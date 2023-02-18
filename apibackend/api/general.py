import json 
import os
import random
import string
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
from apibackend.api.util import allowed_file,sort_tuples,sort1_tuples

@app.route("/intelliq_api/questionnaire/<string:questionnaireid>", methods=['GET'])
def QQID(questionnaireid):
   
    if request.method=='GET':
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
                    query1 = "select Questionnaire_Title from Questionnaire where QuestionnaireID = '{}'".format(questionnaireid)
                    cur.execute(query1)

                    title={}
                    title['questionnaireID']=questionnaireid
                    title['questionnaireTitle'] = cur.fetchall()[0][0]

                    query2 = "select Keywordskeyword from Questionnaire_Keywords where QuestionnaireQuestionnaireID = '{}'".format(questionnaireid)
                    cur.execute(query2)

                    x=cur.fetchall()
                    res2=[]

                    for tup in x:
                        res2.append(tup[0])

                    title['keywords']=res2

                    query3 = "select Question_ID as qID, Qtext as qtext, Qrequired as required, Qtype as type from Question where QuestionaireID = '{}'".format(questionnaireid)
                    cur.execute(query3)
                    
                    col3_names = [j[0] for j in cur.description] 
                    res3 = [dict(zip(col3_names, entry3)) for entry3 in cur.fetchall()]

                    title['questions']=res3
                    
                    if (f=='csv'):
                        new_data=[]
                        for i in title['questions']:
                            new_d=dict()
                            for key,value in title.items():
                                if (not isinstance(value,list)):
                                    new_d[key] = value 
                            
                            for b,value in enumerate(title['keywords']):
                                x=str(b)
                                new_d["keywords_" +x] = value
                            for k, v in i.items():
                                new_d["questions_" + k] = v
                            new_data.append(new_d)
                        
                        csv_columns = new_data[0].keys()
                        
                        csv_data = ",".join(csv_columns) + "\n"   
                        for i in new_data:
                            new_row = list()
                            for col in csv_columns:
                                new_row.append(str(i[col]))
                        
                            csv_data += ",".join(new_row) + "\n"  
                        resp=Response(csv_data,mimetype="text/csv")
                        resp.status_code=200
                    else:
                        resp = jsonify (title)
                        resp.status_code = 200
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


@app.route("/intelliq_api/question/<string:questionnaireid>/<string:questionid>", methods=['GET'])
def QQQID(questionnaireid,questionid):

    if request.method=='GET':
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
                q2 ="select question_id from question where questionaireid ='{}'".format(questionnaireid) 
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
                   
                cur.execute(q2)
                x = cur.fetchall()
                
                qqqids=[]
                for n in x:
                    qqqids.append(n[0])
                if questionid not in qqqids:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Question not in Questionnaire" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"Question not in Questionnaire"})
                        resp.status_code=400
                    return resp

                query1 = "select Question_ID, Qtext, Qrequired, Qtype from Question where (Question_ID = '{}' and questionaireid = '{}')".format(questionid, questionnaireid)
                cur.execute(query1)

                z = cur.fetchall()
                z = list(z[0])

                maindic={}
                maindic['questionnaireID']= questionnaireid
                maindic['qID']=questionid
                maindic['qtext']=z[1]
                maindic['required']=z[2]
                maindic['type']=z[3]
                maindic['options']=[]
                query2 = "select o.opt_id, o.opt_Text, q.next_q from Options as o join Questions_Options as q on (opt_id = optid) where Opt_ID in (select OptID from Questions_Options where QuestionID = '{}')".format(questionid)
                
                cur.execute(query2)
                x=cur.fetchall()
                x=list(x)
                print(x)
                y = sort1_tuples(x)
                print(y)
            
                for queryreturn in y:
                    helpdic={}
                    helpdic['optID']=queryreturn[0]
                    helpdic['opttxt']=queryreturn[1]
                    helpdic['nextqID']=queryreturn[2]
                    maindic['options'].append(helpdic)
                  
                cur.close()
                if (f=='csv'):
                    new_data=[]
                    for i in maindic['options']:
                        new_d=dict()
                        for key,value in maindic.items():
                            if (not isinstance(value,list)):
                                new_d[key] = value                 
                        for k, v in i.items():
                            new_d["answers_" + k] = v
                        new_data.append(new_d)
                    
                    csv_columns = new_data[0].keys()
                  
                    # Generate the first row of CSV 
                    csv_data = ",".join(csv_columns) + "\n"
                    # Generate the single record present
                    for i in new_data:
                        new_row = list()
                        for col in csv_columns:
                            new_row.append(str(i[col]))

                        csv_data += ",".join(new_row) + "\n"  
                    resp=Response(csv_data,mimetype="text/csv")
                    resp.status_code=200
                else:
                    resp=jsonify(maindic)
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
    
    
@app.route("/intelliq_api/doanswer/<string:questionnaireid>/<string:questionid>/<string:session>/<string:optionid>", methods=['POST'])
def doanswer(questionnaireid,questionid,session,optionid):

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
                q1 ="select question_id from question where questionaireid = '{}'".format(questionnaireid)

                q2 ="select optid from questions_options where questionid='{}'".format(questionid)
                
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
                
                cur.execute(q1)
                x = cur.fetchall()
                
                qqids=[]
                for n in x:
                    qqids.append(n[0])
                if questionid not in qqids:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Question not in Questionnaire" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"Question not in Questionnaire"})
                        resp.status_code=400
                    return resp
                
                
                cur.execute(q2)
                x = cur.fetchall()
                
                optids=[]
                for n in x:
                    optids.append(n[0])
                if optionid not in optids:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Invalid Option" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp = jsonify ({"status":"failed", "reason":"Invalid Option"})
                        resp.status_code=400
                    return resp

                if len(session) != 4:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Session format is not valid" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp = jsonify ({"status":"failed", "reason":"Session format is not valid"})
                        resp.status_code=400
                    return resp


                query="select session_id from sesion"
                
                cur.execute(query)
                ses=list()
                
                for n in cur.fetchall():
                    ses.append(n[0])

                active = 0
                
                for n in ses:
                    if session == n:
                        active = 1
                            
                if active == 1:
                    query="select questionnaireid from sesion where session_id= '{}'".format(session)
                    cur.execute(query)
                    q=list()

                    for b in cur.fetchall():
                        q.append(b[0])

                    if q[0] != questionnaireid:
                        if (f=='csv'):
                            csv=""""status","reason"
"failed","Session does not refer to Questionnaire" """
                            resp=Response(csv,mimetype="text/csv")
                            resp.status_code=400
                        else:
                            resp = jsonify ({"status":"failed", "reason":"Session does not refer to Questionnaire"})
                            resp.status_code=400
                        return resp

                    query1="select o_id from session_questions_options where s_id='{}' and q_id='{}'".format(session,questionid)
                    cur.execute(query1)

                    if len(cur.fetchall()) != 0:
                        if (f=='csv'):
                            print("YES")
                            csv=""""status","reason"
"failed","Question already answered in Session" """
                            resp=Response(csv,mimetype="text/csv")
                            resp.status_code=400
                        else:
                            resp = jsonify ({"status":"failed", "reason":"Question already answered in Session"})
                            resp.status_code=400
                        return resp
                    
                elif active == 0:    
                    z = string.ascii_letters
                    for _ in range(10):
                        user = ''.join(random.choice(z) for _ in range(10))      
                    query2="insert into sesion (session_id, questionnaireid, userstring) values ('{}','{}','{}')".format(session, questionnaireid, user)
                    cur.execute(query2)
        
                query3="insert into session_questions_options (s_id, q_id, o_id) values ('{}','{}','{}')".format(session, questionid, optionid)
                cur.execute(query3)
                db.connection.commit()
                cur.close()
                if (f=='csv'):
                    csv=""""""              
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=200
                else:
                    resp = jsonify ()
                    resp.status_code=200
                return resp


            except Exception as e:
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Database Error" """
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=500
                else:
                    resp = jsonify ({"status":"failed", "reason":"Database Error"})
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


@app.route("/intelliq_api/getsessionanswers/<string:questionnaireid>/<string:session>", methods=['GET'])
def getsessionanswers(questionnaireid, session):
    if request.method=='GET':
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
                q2 ="select session_id from sesion where questionnaireid ='{}'".format(questionnaireid)
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
         
                cur.execute(q2)
                x = cur.fetchall()
                
                qqids=[]
                for n in x:
                    qqids.append(n[0])
                if session not in qqids:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Session does not refer to Questionnaire" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp = jsonify ({"status":"failed", "reason":"Session does not refer to Questionnaire"})
                        resp.status_code=400
                    return resp
                
                query1 = ("select Question_ID from Question where QuestionaireID = '{}'").format(questionnaireid)
                cur.execute(query1)
        
                myquestions=[]
                for queryreturn in cur.fetchall():
                    myquestions.append(queryreturn[0])
                
                query2 = "select Q_ID,O_ID from session_questions_options where (S_ID = '{}')".format(session)
                cur.execute(query2)
                x=cur.fetchall()
                x=list(x)
                
                y =sort_tuples(x)
            
        
                maindic={}
                maindic['QuestionnaireID']= questionnaireid
                maindic['session']=session
                maindic['answers']=[]
        
                for queryreturn in y:
                    helpdic={}
                    helpdic['qID']=queryreturn[0]
                    helpdic['ans']=queryreturn[1]
                    maindic['answers'].append(helpdic)
                jsonify(maindic)
                cur.close()
                if (f=='csv'):
                    new_data=[]
                    for i in maindic['answers']:
                        new_d=dict()
                        for key,value in maindic.items():
                            if (not isinstance(value,list)):
                                new_d[key] = value                 
                        for k, v in i.items():
                            new_d["answers_" + k] = v
                        new_data.append(new_d)
                    
                    csv_columns = new_data[0].keys()
                  
                    # Generate the first row of CSV 
                    csv_data = ",".join(csv_columns) + "\n"
                    # Generate the single record present
                    for i in new_data:
                        new_row = list()
                        for col in csv_columns:
                            new_row.append(str(i[col]))

                        csv_data += ",".join(new_row) + "\n"    
                    resp=Response(csv_data,mimetype="text/csv")
                    resp.status_code=200
                else:
                    resp = jsonify (maindic)
                    resp.status_code=200
                return resp
                
            except Exception as e:
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Database Error" """
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=500
                else:
                    resp = jsonify ({"status":"failed", "reason":"Database Error"})
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
   
    
    
@app.route("/intelliq_api/getquestionanswers/<string:questionnaireID>/<string:questionID>",methods=['GET'])
def getquestionanswers(questionnaireID, questionID):

    if request.method=='GET':
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
                q1 ="select question_id from question where questionaireid ='{}'".format(questionnaireID)
                
                cur.execute(query0)
                x = cur.fetchall()
                
                qids=[]
                for n in x:
                    qids.append(n[0])
                if questionnaireID not in qids:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Questionnaire not found" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"Questionnaire not found"})
                        resp.status_code=400
                    return resp
                 
                cur.execute(q1)
                x = cur.fetchall()  
                
                qqids=[]
                for n in x:
                    qqids.append(n[0])
                    
                if questionID not in qqids:
                    if (f=='csv'):
                        csv=""""status","reason"
"failed","Question not in Questionnaire" """
                        resp=Response(csv,mimetype="text/csv")
                        resp.status_code=400
                    else:
                        resp=jsonify({"status":"failed", "reason":"Question not in Questionnaire"})
                        resp.status_code=400
                    return resp
                
                query1 = ("select Question_ID from Question where QuestionaireID = '{}'").format(questionnaireID)
                cur.execute(query1)
                
                myquestions=[]
                for queryreturn in cur.fetchall():
                    myquestions.append(queryreturn[0])
                    
                query2 = "select S_ID,O_ID from session_questions_options where (Q_ID = '{}')".format(questionID)
                cur.execute(query2)
                x=cur.fetchall()
                x=list(x)  
                y=sort_tuples(x) 
                maindic={}
                maindic['QuestionnaireID']= questionnaireID
                maindic['questionid']=questionID
                maindic['answers']=[]
            
                for queryreturn in y:
                    helpdic={}
                    helpdic['session']=queryreturn[0]
                    helpdic['ans']=queryreturn[1]
                    maindic['answers'].append(helpdic)
                cur.close()       
                if (f=='csv'):
                    new_data=[]
                    for i in maindic['answers']:
                        new_d=dict()
                        for key,value in maindic.items():
                            if (not isinstance(value,list)):
                                new_d[key] = value                 
                        for k, v in i.items():
                            new_d["answers_" + k] = v
                        new_data.append(new_d)
                    
                    csv_columns = new_data[0].keys()
                  
                    # Generate the first row of CSV 
                    csv_data = ",".join(csv_columns) + "\n"
                    # Generate the single record present
                    for i in new_data:
                        new_row = list()
                        for col in csv_columns:
                            new_row.append(str(i[col]))

                        csv_data += ",".join(new_row) + "\n"
           
                    resp=Response(csv_data,mimetype="text/csv")
                    resp.status_code=200
                else:
                    resp = jsonify (maindic)
                    resp.status_code=200
                return resp
                
            except Exception as e:
                if (f=='csv'):
                    csv=""""status","reason"
"failed","Database Error" """
                    resp=Response(csv,mimetype="text/csv")
                    resp.status_code=500
                else:
                    resp = jsonify ({"status":"failed", "reason":"Database Error"})
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
   