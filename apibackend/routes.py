import json 
import os
import random
import string
from flask import Flask, render_template, request, flash, redirect, url_for, abort, jsonify, Response
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



@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            admin_username = request.form.get("Username")
            admin_password = request.form.get("password")
            if admin_username == '' or admin_password == '':
                return render_template("BadRequest400.html")

            else:
                return redirect(url_for("Admin"))
        else:
            return render_template("base.html")
        
    except Exception as e:
        print(e)
        abort(500)

@app.route("/error")
def getBase():
    try:
        
        return render_template("error.html")
            
    except Exception as e:
        print(e)
        abort(500)


@app.route("/user", methods=['GET', 'POST'])
def getUser():
    try:
        if request.method == 'POST':
            if request.form['submit_button'] == 'See all Questionnaires':
                cur = db.connection.cursor()  
                cur.execute("select questionnaire_title, questionnaireid from questionnaire")

                collnames = [k[0] for k in cur.description]
                result = [dict(zip(collnames, entry)) for entry in cur.fetchall()]
                return render_template("all_questionnaires.html", result=result)

            elif request.form['submit_button'] == 'Check':
                category=request.form.get("Category")
                cur = db.connection.cursor()
                cur.execute("select Keyword from Keywords")

                column_names = [i[0] for i in cur.description]
                x = cur.fetchall()

                k=0
                for keywords in x:
                    for keyword in keywords:
                        if category == keyword:
                         k=1

                query = "select Questionnaire_Title, questionnaireid from Questionnaire where QuestionnaireID in (select QuestionnaireQuestionnaireID from Questionnaire_Keywords where KeywordsKeyword = '{}')".format(category)
                cur.execute(query)

                col_names = [j[0] for j in cur.description]
                res = [dict(zip(col_names, entry1)) for entry1 in cur.fetchall()]

                if k:
                    return render_template("questionnaire_list.html", res=res)
                else:
                    return render_template("Nodata402.html")

        return render_template("user.html")
                              
    except Exception as e:
        print(e)
        abort(500)
        

@app.route("/firstanswer/<string:qid>",methods=["GET","POST"])
def getFirst(qid):  
        

    try:
        cur = db.connection.cursor()

        query1 = "select question_id from question where questionaireid = '{}' limit 1".format(qid)
        cur.execute(query1)

        x = cur.fetchall()
        questionid = x[0][0]

        s = string.ascii_letters
        for _ in range(10):
            session = ''.join(random.choice(s) for _ in range(4))

        

        z = string.ascii_letters
        for _ in range(10):
            user = ''.join(random.choice(s) for _ in range(10))
        
        query = "insert into sesion (session_id, questionnaireid, userstring) values ('{}', '{}', '{}')".format(session, qid, user)
        cur.execute(query)
        db.connection.commit()

        cur.close()

        return redirect(url_for("getAnswering", qid=qid, questionid=questionid, session=session))
                                 
    except Exception as e:
        print(e)
        abort(500)


@app.route("/answering/<string:qid>/<string:questionid>/<string:session>",methods=["GET","POST"])
def getAnswering(qid,questionid,session):  

    try:
        
            form = MyForm()
            cur = db.connection.cursor()
        
            query = "select Qtext from Question where Question_ID ='{}'".format(questionid)
            cur.execute(query)
        

            column_names = [i[0] for i in cur.description]
     
            question = [dict(zip(column_names, entry1)) for entry1 in cur.fetchall()]

            query2 = "select Opt_text, Opt_ID from options where opt_id in (select optid from questions_options where questionid = '{}') ".format(questionid) 
            cur.execute(query2)

            col_names = [j[0] for j in cur.description]

            options = [dict(zip(col_names, entry2)) for entry2 in cur.fetchall()]


            cur.close()

            return render_template("answering.html", qid=qid, questionid=questionid, session=session,question=question, options=options, form=form)
                                 
    except Exception as e:
        print(e)
        abort(500)

@app.route("/next/<string:qid>/<string:questionid>/<string:session>", methods=['POST'])
def getNext(qid,questionid,session):
    try:
        
        form=MyForm()

        if request.method=="POST" and form.validate_on_submit():
            un = request.form['options']
            
            cur = db.connection.cursor()

            query2="insert into session_questions_options (q_id,s_id,o_id) values ('{}','{}','{}')".format(questionid,session,un)
            cur.execute(query2)

            db.connection.commit()

            query = "select next_q from questions_options where optid='{}'".format(un)

            cur.execute(query)
            

            column_names=[i[0] for i in cur.description]
        
            res=[dict(zip(column_names, entry)) for entry in cur.fetchall()]
            next = res[0]['next_q']
            cur.close()

            if next == questionid:
                return redirect(url_for("getAnswered",session=session))   
           
            return redirect(url_for ("getAnswering",qid=qid,questionid=next,session=session))

    except Exception as e:
        return redirect(url_for("getBase"))


@app.route("/answered/<string:session>")
def getAnswered(session):
    try:

        return render_template("answered.html", session=session)
                             
    except Exception as e:
        print(e)
        abort(500)

@app.route("/summary/<string:session>")
def getSummary(session):
    try:
        cur = db.connection.cursor()

        cur.execute("select qtext from question where question_id in (select q_id from session_questions_options where s_id = '{}')".format(session))

        column_names = [i[0] for i in cur.description]
     
        res = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

        cur.execute("select opt_text from options where opt_id in (select o_id from session_questions_options where s_id = '{}')".format(session))

        col_names = [j[0] for j in cur.description]
     
        result = [dict(zip(col_names, entry1)) for entry1 in cur.fetchall()]

        for i, dic in enumerate(res):
            dic['opt_text']=result[i]['opt_text']

        cur.close()

        return render_template("summary.html", res=res)
                             
    except Exception as e:
        print(e)
        abort(500)


@app.route("/admin")
def Admin():
    try:
        return render_template("admin.html")                     
    except Exception as e:
        print(e)
        abort(500)

@app.route("/keyword", methods=['GET', 'POST'])
def Keyword():
    try:
        if request.method == 'POST':
            q_keyword = request.form.get("Question_keywords")
            if q_keyword == '':
                return render_template("emptykeyword.html")

            else:
                cur = db.connection.cursor()
                cur.execute("select Keyword from Keywords")

                column_names = [i[0] for i in cur.description]
                x = cur.fetchall()

                k=0
                for keywords in x:
                    for keyword in keywords:
                        if q_keyword == keyword:
                         k=1

                if k:
                    query="select Question_ID, Qtext from Question where QuestionaireID in (select QuestionnaireQuestionnaireID from Questionnaire_Keywords where KeywordsKeyword = '{}')".format(q_keyword)
                    cur.execute(query)

                    col_names = [i[0] for i in cur.description]
                    res = [dict(zip(col_names, entry1)) for entry1 in cur.fetchall()]
                    return render_template("keywordresults.html", res=res)

                else:
                    return render_template("badquestionrequest.html")

        else:
            return render_template("keywordquestions.html")                      
    except Exception as e:
        print(e)
        abort(500)
    
@app.route('/upload/<string:name>/<string:state>', methods = ['GET'])  
def success(name,state): 
    try:
        if request.method == 'GET':
            return render_template("Acknowledgement.html", name=name, state=state)
    except Exception as e:
        print(e)
        abort(500)

  
#redirection upon successfull upload of the allowed files
@app.route('/inserting/<string:name>', methods = ['GET'])  
def inserting(name):  
    if request.method == 'GET':
        try:
            path='./apibackend/'+name
            with open(path,'r', encoding='utf-8') as file:
                data=json.load(file)
                cur= db.connection.cursor()
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
            state ="successfully added questionnaire"
            return redirect(url_for('success', name=name, state=state))
        except Exception as e:
            print(e)
            state =" was **NOT** added to the database -- WRONG JSON FORMAT"
            return redirect(url_for('success', name=name, state=state))
    return render_template('error500.html')
              
        
          
 
#process of file upload in /questionnaire_upd
#def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/questionnaire_upd', methods=['GET', 'POST'])
def upload_file():
    try:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                return render_template("questionnaire_upd.html",info="You need to select a file")
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                return render_template("questionnaire_upd.html",info="You need to select a file")
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #print(filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('inserting', name=filename))
            else:
                return render_template("questionnaire_upd.html",info="*Error: Only file type '.json' is allowed")
        return render_template("questionnaire_upd.html")
    except Exception as e:
        print(e)
        abort(500)

# create and Download json File with all answers of questionnaire


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    try:
        path = filename
        
        return send_file(path, as_attachment=True)
    except Exception as e:
        print(e)
        abort(500)

    
@app.route('/dnld/<string:QuestionnaireID>')
def mkjson(QuestionnaireID):
    try:
        mydict={}
        mydict['questionnaireID']=QuestionnaireID
        cur = db.connection.cursor()
        query1 = ("select Question_ID from Question where QuestionaireID = '{}'").format(QuestionnaireID)
        cur.execute(query1)
        myquestions=[]
        for queryreturn in cur.fetchall():
            myquestions.append(queryreturn[0])

        questions=[]
        for qqid in myquestions:
            query2 = "select S_ID,O_ID from session_questions_options where (Q_ID = '{}')".format(qqid)
            cur.execute(query2)
            x=cur.fetchall()     
            maindic={}
            maindic['questionid']=qqid
            maindic['answers']=[]
            for queryreturn in x:
                helpdic={}
                helpdic['session']=queryreturn[0]
                helpdic['ans']=queryreturn[1]
                maindic['answers'].append(helpdic)
            questions.append(maindic)
        mydict['questions']=questions
        path = './apibackend/'+QuestionnaireID+'.json'
        File1 = open(path, "w+")
        json.dump(mydict,File1,ensure_ascii=False,indent=2,sort_keys=False)
        File1.close()
        path = QuestionnaireID+'.json'
        return  redirect (url_for ("download",filename=path))
    except Exception as e:
        print(e)
        abort(500)



@app.route("/getquestionnaires")
def getquestionnaires():
    try:
        cur = db.connection.cursor()

        cur.execute("select QuestionnaireID, Questionnaire_Title from Questionnaire")

        column_names = [i[0] for i in cur.description]
     
        Questionnaire = [dict(zip(column_names, entry1)) for entry1 in cur.fetchall()]

        cur.close()
        return render_template("getquestionnaires.html",Questionnaire=Questionnaire)
    except Exception as e:
        print(e)
        abort(500)
    

@app.route("/getquestionnaires/<string:QuestionnaireID>")
def Questions(QuestionnaireID):
        try:
            cur = db.connection.cursor()
            query="select Question_ID ,Qtext from Question where QuestionaireID ='{}'".format(QuestionnaireID)
            
            cur.execute(query)

            column_names = [i[0] for i in cur.description]
     
            Questions = [dict(zip(column_names, entry1)) for entry1 in cur.fetchall()]

            cur.close()

            return render_template("getquestions.html",Questions=Questions, QID= QuestionnaireID)
                                                                
        except Exception as e:
            print(e)
            abort(500)

@app.route("/getquestionnaires/<string:QuestionnaireID>/<string:Question_ID>")
def Answers(QuestionnaireID, Question_ID):
        try:
            
            cur = db.connection.cursor()
            
            query1="select O_ID from session_questions_options where Q_ID = '{}'".format(Question_ID)

            cur.execute(query1)

            column_names = [i[0] for i in cur.description]
     
            Answers = [dict(zip(column_names, entry1)) for entry1 in cur.fetchall()]
            l=[]
            for x in Answers: 
                l.append(x['O_ID'])
            
            
            dic={}                
            for i in l:
                if i not in dic.keys():
                    dic[i]=1
                else:
                    dic[i]+=1        
            query="select Opt_text, Opt_ID from options where Opt_ID in (select O_ID from session_questions_options where Q_ID = '{}')".format(Question_ID)
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
     
            Answers = [dict(zip(column_names, entry1)) for entry1 in cur.fetchall()]
            for x in Answers:
                for y in dic.keys():
                    if x['Opt_ID']==y:
                        x['Count']=dic[y]

            cur.close()

            return render_template("getanswers.html",Answers=Answers,QuestionnaireID=QuestionnaireID)
                                                                
        except Exception as e:
            print(e)
            abort(500)

@app.errorhandler(400)
def page_not_found(e):
    # note that we set the 400 status explicitly
    return render_template("400.html", pageTitle = "Bad Request"),400

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html", pageTitle = "Not Found"),404

@app.errorhandler(405)
def method_not_allowed(e):
    # note that we set the 404 status explicitly
    return render_template("405.html", pageTitle = "Not Allowed"),405


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html", pageTitle = "Internal Server Error"),500