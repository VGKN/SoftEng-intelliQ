import json 
import os
import random
import string
import csv
from flask import Flask, render_template, request, flash, redirect, url_for, abort, jsonify, Response,make_response
from flask_mysqldb import MySQL
from apibackend import app, db,ALLOWED_EXTENSIONS ## initially created by __init__.py, need to be used here
from apibackend.forms import MyForm,FieldForm,ProjectForm,QuestionForm
from jinja2 import Template
from werkzeug.utils import secure_filename
from flask import send_file
from flask import send_from_directory
from flask import current_app
from collections import ChainMap
from operator import itemgetter
from apibackend.api.util import allowed_file


#healthcheck endpoint            
@app.route("/intelliq_api/admin/healthcheck", methods=['GET'])
def healthcheck():

    if request.method=='GET':
        f=request.args.get('format')
 
        if (f is None or f=='json'):
            try:
                cur = db.connection.cursor() #database connected
                resp=jsonify({"status":"OK", "dbconnection":"MySQL Database intelliQ running on Apache Web Server"}) 
                resp.status_code=200
                return resp
            except Exception as e: #not connected to database
                print(e)
                resp = jsonify({"status":"failed","dbconnection":"MySQL Database intelliQ not connected"})
                resp.status_code=500
                return resp
                
        elif f=='csv':
            try:
                cur = db.connection.cursor() #database connected
                csv=""""status","dbconnection"
"OK","MySQL Database intelliQ running on Apache Web Server" """
                resp=Response(csv,mimetype="text/csv")
                resp.status_code=200
                return resp
                
            except Exception as e: #not connected to database
                print(e)
                csv=""""status","dbconnection"
"failed","MySQL Database intelliQ not connected" """
                resp=Response(csv,mimetype="text/csv")
                resp.status_code=500
                return resp
        else: #checking for the format
            resp=jsonify({"status":"failed", "reason":"Only csv and json format is allowed"}) 
            resp.status_code=400
            return resp
    else: #if method is POST
        resp=jsonify({"status":"failed","reason":"Method Not Allowed"}) 
        resp.status_code=400
        return resp
                                 


@app.route("/intelliq_api/admin/questionnaire_upd", methods=["POST"])
def questionnaire_upd():

    if request.method=='POST':
    
        f=request.args.get('format')
        if (f is None or f=='json' or f=='csv'):
            try:
                cur = db.connection.cursor()
            except: #if database not connected
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Cannot connect to Database" """
                    
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=500
                else:
                    resp=jsonify({"status":"failed", "reason":"Cannot connect to Database"})
                    resp.status_code=500
                return resp
                
            try:
                success=False
                errors={}
                
                if 'file' not in request.files:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","No file part in request header" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"No file part in request header"})
                        resp.status_code=400
                    return resp
                    
                file=request.files.getlist('file')
                count=0
                
                for fil in file:
                    count+=1
                    if fil and allowed_file(fil.filename):
                        filename=secure_filename(fil.filename)
                        fil.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                        success=True
                    else:
                        errors['ERROR']='FILE TYPE IS NOT ALLOWED'
                
                if count !=1:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Server can only process one .json file" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"Server can only process one .json file"})
                        resp.status_code=400
                    return resp
                   
                        
                if success and errors:
                    if (f=='csv'):
                            csv=""""status","reason"
"failed","Database Error" """
                            resp=Response(csv,mimetype="text/csv")
                            resp.status_code=500
                    else:
                        resp=jsonify({"status":"failed", "reason":"Database Error"})
                        resp.status_code=500
                    return resp
                    
                if success:
                    path='./apibackend/'+fil.filename
                    with open(path,'r', encoding='utf-8') as file:
                        data=json.load(file)
                        
                        query="INSERT INTO Questionnaire (questionnaireID, questionnaire_Title, Aid) VALUES ('{}','{}',1);".format(data['questionnaireID'],data['questionnaireTitle'])
                        cur.execute(query)
                        cur.execute("Select Keyword from keywords")
                        Keywords=cur.fetchall()
                        for keyword in data['keywords']:
                            if keyword not in Keywords:
                                query="INSERT INTO Keywords (keyword) VALUES ('{}');".format(keyword)
                                cur.execute(query)
                            query="INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('{}','{}');".format(data['questionnaireID'],keyword)
                            cur.execute(query)
                        for questions in data['questions']:
                            myx=[]
                            myy=[]
                            qtext=[]
                            texts=[]
                            x=questions['qtext'].find("[*")
                            myx.append(x)
                            y=questions['qtext'].find("]",x+2)
                            myy.append(y)
                            while(x!=-1):
                                qtext.append(questions['qtext'][x+2:y])
                                x=questions['qtext'].find("[*", y)
                                myx.append(x)
                                y=questions['qtext'].find("]",x+2)
                                myy.append(y)
                            if len(qtext)!=0:
                                for question in data['questions']:
                                    if question['qID ']==qtext[1]:
                                        texts.append(question['qtext'])
                                    for options in question['options']:
                                        if options['optID']==qtext[0]:
                                            texts.append(options['opttxt'])
                                questiontext=questions['qtext'][0:myx[0]]+"\\'"+texts[1]+"\\'"+questions['qtext'][myy[0]+1:myx[1]] +"\\'"+texts[0]+"\\'"+questions['qtext'][myy[1]+1:]          
                                query="INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('{}','{}','{}','{}','{}');".format(questions['qID '],questiontext,questions['required'],questions['type'],data['questionnaireID'])
                            else:
                                query="INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('{}','{}','{}','{}','{}');".format(questions['qID '],questions['qtext'],questions['required'],questions['type'],data['questionnaireID'])
                            cur.execute(query)  
                            nextq=''
                        for questions in data['questions']:
                            for option in questions['options']:
                                query="INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('{}','{}');".format(option['optID'], option['opttxt'])
                                cur.execute(query)
                                if option['nextqID']=='-':
                                    nextq=questions['qID ']
                                else:
                                    nextq=option['nextqID']
                                query="INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('{}','{}','{}');".format(questions['qID '], option['optID'], nextq)
                                cur.execute(query)
                        db.connection.commit()
                        
                        if (f=='csv'):
                            csv=""""status","state"
"OK","Questionnaire successfully uploaded" """
                            resp=Response(csv,mimetype="text/csv")
                            resp.status_code=200
                        else:      
                            resp=jsonify({"status":"OK","state":"Questionnaire successfully uploaded"})
                            resp.status_code=200
                        return resp
                else:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Wrong file format" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"Wrong file format"})
                        resp.status_code=400
                    return resp                       
            except Exception as e:
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Wrong json format, questionnaire not uploaded" """
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=400
                else:
                    resp=jsonify({"status":"failed","reason":"Wrong json format, questionnaire not uploaded"})
                    resp.status_code=400
                return resp    
                
        else:
            resp=jsonify({"status":"failed", "reason":"Only csv and json format is allowed"}) 
            resp.status_code=400
            return resp

    else:
        resp=jsonify({"status":"failed","reason":"Method Not Allowed"})
        resp.status_code=400
        return resp
    
      
    
@app.route("/intelliq_api/admin/resetall", methods=["POST"])
def postResetAll():

    if request.method == 'POST':
        
        f=request.args.get('format')
        if (f is None or f=='json' or f=='csv'):
                
            try:
                cur = db.connection.cursor()
            except: #if database connected
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Cannot connect to Database" """
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=500
                else:
                    resp=jsonify({"status":"failed", "reason":"Cannot connect to Database"})
                    resp.status_code=500
                return resp
                
            try:
                cur.execute("DELETE FROM Questionnaire_Keywords")
                cur.execute("DELETE FROM Questions_Options")
                cur.execute("DELETE FROM Session_Questions_Options")
                cur.execute("DELETE FROM Question")
                cur.execute("DELETE FROM Sesion")
                cur.execute("DELETE FROM Questionnaire")
                cur.execute("DELETE FROM Keywords")
                cur.execute("DELETE FROM Options")
                db.connection.commit()
                cur.close()
            except Exception as e:
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Database error" """
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=500
                else:
                    resp=jsonify({"status":"failed", "reason": "Database error"})
                    resp.status_code=500
                return resp
            if (f=='csv'):
                csv=""""status"
"OK" """
                resp=Response(csv,mimetype="text/csv")
                resp.status_code=200
            else:
                resp=jsonify({"status":"OK"})
                resp.status_code=200
            return resp
                                   
        else:
            resp=jsonify({"status":"failed", "reason":"Only csv and json format is allowed"}) 
            resp.status_code=400
            return resp

    else:
        resp=jsonify({"status":"failed","reason":"Method Not Allowed"})
        resp.status_code=400
        return resp


@app.route("/intelliq_api/admin/resetq/<string:questionnaireid>", methods=['POST'])
def resetq(questionnaireid):
    
    if request.method=='POST':
        f=request.args.get('format')
        if (f is None or f=='json' or f=='csv'):
        
            try:
                cur = db.connection.cursor()
            except:
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Cannot connect to Database" """
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=500
                else:
                    resp=jsonify({"status":"failed", "reason":"Cannot connect to Database"})
                    resp.status_code=500
                return resp
                
                
            try:
                query0 = "select questionnaireid from questionnaire"
                cur.execute(query0)
                x = cur.fetchall()
                qids=[]
                for n in x:
                    qids.append(n[0])
                if questionnaireid not in qids:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Questionnaire not found" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"Questionnaire not found"})
                        resp.status_code=400
                    return resp
      
                else:
                    query = "delete from session_questions_options where q_id in (select question_id from question where questionaireid ='{}')".format(questionnaireid)
                    cur.execute(query)
                    query=  "delete from sesion where questionnaireid='{}'".format(questionnaireid)
                    cur.execute(query)
                    db.connection.commit()
                    cur.close()
                    if (f=='csv'):
                        csv=""""status"
"OK" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=200
                    else:
                        resp=jsonify({"status":"OK"})
                        resp.status_code=200
                    return resp  
                    
            except Exception as e:
                if (f=='csv'):
                        csv=""""status","reason"
"failed","Database Error" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=500
                else:
                    resp=jsonify({"status":"failed", "reason":"Database Error"})
                    resp.status_code=500
                return resp   
                
        else:
            resp=jsonify({"status":"failed", "reason":"Only csv and json format is allowed"}) 
            resp.status_code=400
            return resp        
    else:
        resp=jsonify({"status":"failed","reason":"Method Not Allowed"})
        resp.status_code=400
        return resp
