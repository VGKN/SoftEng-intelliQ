from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from apibackend import app, db,ALLOWED_EXTENSIONS ## initially created by __init__.py, need to be used here
from apibackend.forms import MyForm,FieldForm,ProjectForm
import os
from werkzeug.utils import secure_filename
from flask import send_file
from flask import send_from_directory
from flask import current_app

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            admin_username=request.form.get("Username")
            admin_password=request.form.get("password")
            if admin_username == '' or admin_password == '':
                return render_template("BadRequest400.html",pageTitle="Landing Page")

            else:
                return render_template("admin.html",pageTitle="Landing Page")    
        else:
            return render_template("base.html",pageTitle="Landing Page")    
         #                      
    except Exception as e:
        print(e)
        abort(500)

@app.route("/user", methods=['GET', 'POST'])
def getUser():
    try:
        if request.method == 'POST':
            if request.form['submit_button'] == 'See all Questionnaires':
                #return render_template("base.html",pageTitle="Landing Page")
                cur = db.connection.cursor()
                query1="select Questionnaire_Title from questionnaire"  
                cur.execute(query1)

                collnames = [k[0] for k in cur.description]
                result = [dict(zip(collnames, entry)) for entry in cur.fetchall()]
                return render_template("all_questionnaires.html", result=result, pageTitle="Welcome user")

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

                query = "select Questionnaire_Title from Questionnaire where QuestionnaireID in (select QuestionnaireQuestionnaireID from Questionnaire_Keywords where KeywordsKeyword = '{}')".format(category)
                cur.execute(query)

                col_names = [j[0] for j in cur.description]
                res = [dict(zip(col_names, entry1)) for entry1 in cur.fetchall()]

                if k:
                    return render_template("questionnaire_list.html", res=res, pageTitle="Welcome user")
                else:
                    return render_template("Nodata402.html",pageTitle="Landing Page")

        return render_template("user.html",pageTitle="Landing Page")
                              
    except Exception as e:
        print(e)
        return render_template("user.html",pageTitle="Landing Page")

@app.route("/answering")
def getAnswering():
    try:
        cur = db.connection.cursor()
        questionnairee='QQ000'
        
        query = "select Qtext from Question where QuestionaireID ='{}' limit 1".format(questionnairee)
        print(query)
        cur.execute(query)
        

        column_names = [i[0] for i in cur.description]
     
        question = [dict(zip(column_names, entry1)) for entry1 in cur.fetchall()]

        query1 = "select question_id from question where questionaireid = '{}' limit 1".format(questionnairee)
        cur.execute(query1)

        x = cur.fetchall()
        myx = x[0][0]

        query2 = "select Opt_text from options where opt_id in (select optid from questions_options where questionid = '{}') ".format(myx) 
        cur.execute(query2)

        col_names = [j[0] for j in cur.description]

        options = [dict(zip(col_names, entry2)) for entry2 in cur.fetchall()]
        print(options)

        cur.close()

        return render_template("answering.html", question=question, options=options)
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html")

@app.route("/answered")
def getAnswered():
    try:
        #cur = db.connection.cursor()
        #cur.execute("select Qtext from question where questionnaire_id = {}".format(number))

        #column_names = [i[0] for i in cur.description]
     
        #res = [dict(zip(column_names, entry)) for entry in cur.fetchall()]

        #cur.execute("select Qtext from question where questionnaire_id = {}".format(number))

        return render_template("answered.html", pageTitle="Welcome user")
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")

@app.route("/admin")
def getOrgs():
    try:
        return render_template("admin.html", pageTitle="Admin", name= "admin name")
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")
    
#redirection upon successfull upload of the allowed files
@app.route('/success', methods = ['GET'])  
def success():  
    if request.method == 'GET': 
       return render_template("Acknowledgement.html")
    
#process of file upload in /questionnaire_upd
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/questionnaire_upd', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('success', name=filename))
    return render_template("questionnaire_upd.html",pageTitle="Upload Questionnaire")

#Download File
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    path = filename
    # Returning file from appended path
    return send_file(path, as_attachment=True)


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
        return render_template("base.html",pageTitle="Landing Page")
    

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
            return render_template("base.html",pageTitle="Landing Page")

@app.route("/getquestionnaires/<string:QuestionnaireID>/<string:Question_ID>")
def Answers(QuestionnaireID, Question_ID):
        try:
            
            cur = db.connection.cursor()
            query="select Opt_text, Opt_ID from options where Opt_ID in (select O_ID from session_questions_options where Q_ID = '{}')".format(Question_ID)
            query1="select O_ID from session_questions_options where Q_ID = '{}'".format(Question_ID)

            cur.execute(query)
            cur.execute(query1)

            column_names = [i[0] for i in cur.description]
     
            Answers = [dict(zip(column_names, entry1)) for entry1 in cur.fetchall()]
            l=[]
            for x in Answers: 
                l.append(x['O_ID'])
            print(l)
            dic={}
            for i in l:
                if i not in dic.keys():
                    dic[i]=1
                else:
                    dic[i]+=1
    
            print(Answers)


            cur.close()

            return render_template("getanswers.html",Answers=Answers)
                                                                
        except Exception as e:
            print(e)
            return render_template("base.html",pageTitle="Landing Page")


@app.route("/healthcheck", methods=["GET"])
def getStatus():
    try:

        #r= requests.get()
        
        #data = r.json()
         
        ## create connection to database
        cur = db.connection.cursor()
        cur.execute("create VIEW no_deliverables as ( select RESEARCHER_ID from works_in where project_title in (SELECT t1.project_title  FROM project t1  LEFT JOIN deliverables t2 ON t2.project_title = t1.project_title WHERE t2.project_title IS NULL))")
        cur.execute("SELECT r.researcher_name, r.researcher_lastname, COUNT(w.researcher_id) as project_with_no_deliverables FROM  researcher r   INNER JOIN no_deliverables w ON w.researcher_id = r.researcher_id GROUP BY w.researcher_id  HAVING project_with_no_deliverables >= 5 ORDER BY project_with_no_deliverables DESC")
        ## execute query
       
        column_names = [i[0] for i in cur.description]
     
        res = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.execute("DROP VIEW no_deliverables")
        cur.close()
        return render_template("healthcheck.html",tablename1=tablename1,res=res,pageTitle="Connection Status")                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")
        
      
  
#@app.route("/questionnaire_upd")
#def getCouples():
 #   try:
#
 #       return render_template("questionnaire_upd.html",pageTitle="Upload Questionnaire")
         #                      
  #  except Exception as e:
   #     print(e)
    #    return render_template("frontend/templates/base.html",pageTitle="Landing Page")
        
        
@app.route("/resetall", methods=["POST"])
def getResearcher():
    try:
        tablename1="Young Researchers"
        cur = db.connection.cursor()

        cur.execute("CREATE VIEW current_workers AS SELECT researcher_id AS id FROM Works_in WHERE researcher_id IN (SELECT researcher_id FROM Works_in WHERE project_title IN (SELECT project_title FROM Project WHERE (project_start < CURDATE() AND project_end > CURDATE())))")

        cur.execute("CREATE VIEW current_researchers AS SELECT Researcher.researcher_name, Researcher.researcher_lastname, current_workers.id FROM Researcher INNER JOIN current_workers ON Researcher.researcher_id=current_workers.id")

        cur.execute("SELECT *, COUNT(*) AS spots_in_projects FROM current_researchers WHERE id IN (SELECT researcher_id FROM Researcher WHERE (TIMESTAMPDIFF(YEAR, researcher_birthdate,CURDATE()) < 40)) GROUP BY id ORDER BY spots_in_projects DESC LIMIT 5")
        column_names = [i[0] for i in cur.description]
        researchers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.execute("DROP ViEW current_workers")
        cur.execute("DROP VIEW current_researchers")

        cur.close()
        return render_template("resetall.html",researchers=researchers,tablename1=tablename1,pageTitle="Purge")
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")
        
        
        
@app.route("/resetq", methods=["POST"])
def getAdmins():
    try:
        tablename1="Top 5 Admins by amount of funding given"
        cur = db.connection.cursor()
        cur.execute("CREATE VIEW best_admin AS SELECT admins.admin_name, admins.admin_id, project.org_name as private_company_name, project.budget as budget  FROM Admins INNER JOIN project ON admins.admin_id = project.admin_id WHERE project.org_name IN (SELECT org_name FROM private_company) ORDER BY project.budget DESC")

        cur.execute("SELECT admin_name, private_company_name, SUM(budget) as total_funds FROM best_admin GROUP BY Admin_id ORDER BY total_funds DESC LIMIT 5")

   
        column_names = [i[0] for i in cur.description]

        admins = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.execute("DROP VIEW best_admin")
        cur.close()
        return render_template("resetq.html",admins=admins,tablename1=tablename1,pageTitle="Clear All Answers")
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")
        
        
@app.route("/getquestionanswers/<string:questionnaireID>/<string:questionID>",methods=["GET"])
def Questionss():
    try:
        if request.method=="GET":
            try:
                return render_template("admin.html")
                                                                
            except Exception as e:
                        ## if the connection to the database fails, return HTTP response 500
                flash(str(e), "danger")
                abort(500)
        
    #else: 
       # try:
            ## create connection to database
           # cur = db.connection.cursor()
            ## execute query
           #cur.execute("SELECT * FROM Project")
            #column_names = [i[0] for i in cur.description]
            #table = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            #cur.close()
            #return render_template("query.html",table=table,tablename1="Projects",pageTitle="Show Projects based on criteria",form = form)
                                                           
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")
            

@app.route("/answers_ui")
def getAnswersui():
    try:
        return render_template("answers_ui.html",pageTitle="Landing Page")
         #                      
    except Exception as e:
        print(e)
        return render_template("answers_ui.html",pageTitle="Landing Page")


@app.route("/getsessionanswers")
def getAnswers():
    try:
        return render_template("getsessionanswers.html",pageTitle="Landing Page")
         #                      
    except Exception as e:
        print(e)
        return render_template("getsessionanswers.html",pageTitle="Landing Page")
        
@app.route("/getsessionanswers/<int:questionnaire_id>", methods=["GET"])
def getAnswersS(questionnaire_id):
    try:
         #cur = db.connection.cursor()
         #cur.execute("SELECT * from QUESTIONNAIRE where questionnaireid={}".format(questionnaire_id))
         #column_names = [i[0] for i in cur.description]
         #table = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
         #return jsonify(table)
         return {'success':'ok'}
         #                      
    except Exception as e:
        print(e)
        return {'success':'ok'}

        
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"),404

@app.errorhandler(500)
def server_error(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"),500

