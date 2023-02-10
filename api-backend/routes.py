from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from dbdemo import app, db ## initially created by __init__.py, need to be used here
from dbdemo.forms import MyForm,FieldForm,ProjectForm
import requests

@app.route("/")
def index():
    try:
        return render_template("base.html",pageTitle="Landing Page")
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")


@app.route("/user")
def getUser():
    try:
        tablename1="Welcome user"
        cur = db.connection.cursor()
        
        cur.execute("SELECT Questionnaire_Title FROM Questionnaire")
        column_names = [i[0] for i in cur.description]
        Questionnaires = [dict(zip(column_names, entry)) for entry in cur.fetchall()]     
        cur.close()
        return render_template("user.html",Questionnaires=Questionnaires,tablename1=tablename1,pageTitle="Welcome user")
        
@app.route("/admin")
def getOrgs():
    try:
        cur = db.connection.cursor()
        
        cur.execute("")
        cur.execute("")   
        cur.close()
        return render_template("admin.html", pageTitle="Admin", name= "admin name")
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")

@app.route("/healthcheck", methods=["GET"])
def getStatus():
    try:

        r= requests.get()
        
        data = r.json()
         
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
        
      
  
@app.route("/questionnaire_upd", methods=["POST"])
def getCouples():
    try:
        tablename1="Couples"
        cur = db.connection.cursor()
        cur.execute("CREATE VIEW Couples AS SELECT c.field_name AS Field1, a.field_name AS Field2 FROM Project_Field c, Project_Field a WHERE (a.field_name > c.field_name AND c.project_title IN (SELECT Project_title FROM Project) AND  a.project_title IN (SELECT Project_title FROM Project) AND a.project_title=c.project_title)")

        cur.execute("SELECT Field1, Field2, COUNT(*) AS occurences FROM Couples GROUP BY Field1, Field2 ORDER BY occurences DESC LIMIT 3")
        
        column_names = [i[0] for i in cur.description]
  
        Couples = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        for id,couple in enumerate(Couples):
            couple["Ranking"]=id
        cur.execute("DROP VIEW Couples")   
        cur.close()
        return render_template("questionnaire_upd.html",Couples=Couples,tablename1=tablename1,pageTitle="Upload Questionnaire")
         #                      
    except Exception as e:
        print(e)
        return render_template("base.html",pageTitle="Landing Page")
        
        
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
        
        
@app.route("/createquestionnaire",methods=["GET","POST"])
def getquery():
    form=ProjectForm()
    
        
    if request.method=="POST" and form.validate_on_submit():
         
        forma=form.__dict__
        admin=forma["admin_id"].data
        date=forma["date"].data
        duration=forma["duration"].data
        try:
            
            
            cur = db.connection.cursor()
            if date == "" and duration == "" and admin == "":
                cur.execute("SELECT * FROM Project")
                

            if date != "" and duration != "" and admin != "":
                cur.execute("SELECT * FROM Project WHERE project_start < '{}' AND project_end > '{}' AND duration = '{}' AND admin_id = '{}' ".format(date, date, duration, admin))
                

            elif date != "" and duration != "" and admin == "":
                cur.execute("SELECT * FROM Project WHERE project_start < '{}' AND project_end > '{}' AND duration = '{}' ".format(date, date, duration))
               

            elif date != "" and duration == "" and admin != "":
                cur.execute("SELECT * FROM Project WHERE project_start < '{}' AND project_end > '{}' AND admin_id = '{}' ".format(date, date, admin))
               

            elif date == "" and duration != "" and admin != "":
                cur.execute("SELECT * FROM Project WHERE duration = '{}' AND admin_id = '{}' ".format(duration, admin))
                

            elif date != "" and duration == "" and admin == "":
                cur.execute("SELECT * FROM Project WHERE project_start < '{}' AND project_end > '{}' ".format(date, date))
               

            elif date == "" and duration != "" and admin == "":
                cur.execute("SELECT * FROM Project WHERE duration = '{}' ".format(duration))
               

            elif date == "" and duration == "" and admin != "":
                cur.execute("SELECT * FROM Project WHERE admin_id = '{}' ".format(admin))
                
            column_names=[i[0] for i in cur.description]
            print(column_names)
            table=[dict(zip(column_names, entry)) for entry in cur.fetchall()]
            print(table)
            cur.close()


            return render_template("createquestionnaire.html",table=table,tablename1="Projects",pageTitle="Show Projects based on criteria",form = form)
                                                           
        except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
            flash(str(e), "danger")
            abort(500)
    
    else: 
        try:
            ## create connection to database
            cur = db.connection.cursor()
            ## execute query
            cur.execute("SELECT * FROM Project")
            column_names = [i[0] for i in cur.description]
            table = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()
            return render_template("query.html",table=table,tablename1="Projects",pageTitle="Show Projects based on criteria",form = form)
                                                           
        except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
            flash(str(e), "danger")
            abort(500)
            
@app.route("/query1",methods=["GET","POST"])
def getquery1():
        form=FieldForm()
        if request.method=="POST" and form.validate_on_submit():
                
            field=form.__dict__
            x=field["field"].data
            return redirect(url_for("getALLRESEARCHERS",title=x))
        else: 
            return render_template("projects.html",pageTitle="Insert Project Title",form=form)      
        
      
@app.route("/query1/projects/<title>")
def getALLRESEARCHERS(title):
    
        
        query="SELECT researcher_id, researcher_name, researcher_lastname ,researcher.org_name from researcher where researcher_id in (select researcher_id from Works_in where project_title='{}')".format(title)
        tablename1="Title: {}".format(title)
        try:
        
            ## create connection to database
            cur = db.connection.cursor()
            ## execute query
            cur.execute(query)
            
            column_names = [i[0] for i in cur.description]
            table = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()

            return render_template("showresearchers.html",tablename1=tablename1,table=table,pageTitle="Show  Researchers based on Project")
             #                      
        except Exception as e:
            print(e)
            return render_template("projects.html",pageTitle="Insert Project Title")  

            
@app.route("/programs")
def getPrograms():
       
        try:
           
            ## create connection to database
            cur = db.connection.cursor()
            ## execute query
            cur.execute("SELECT * FROM Program")
            
            column_names = [i[0] for i in cur.description]
           
            table = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()

            return render_template("programs.html",table=table,tablename1="Programs",pageTitle="Show all available Programs")
                                   
        except Exception as e:
            print(e)
            return redirect(url_for("index"))               

@app.route("/fields",methods=["GET","POST"])
def getField():
    form=FieldForm()
    if request.method=="POST" and form.validate_on_submit():
        
        field=form.__dict__
        x=field["field"].data
        return redirect(url_for("getFieldss",fieldname=x))
    else: 
        return render_template("fields.html",pageTitle="Insert interesting Field",form = form)      
                                                           
      
@app.route("/fields/<fieldname>")
def getFieldss(fieldname):
    
    
        query="SELECT * FROM Works_in WHERE Project_title IN (SELECT Project_title FROM Project WHERE (project_start < DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND project_end > CURDATE() ) AND Project_title IN (SELECT project_title FROM Project_Field WHERE (field_name='{}')))".format(fieldname)
        tablename1="Field: {}".format(fieldname)
        try:
        
            ## create connection to database
            cur = db.connection.cursor()
            ## execute query
            cur.execute(query)
            
            column_names = [i[0] for i in cur.description]
            table = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()

            return render_template("showfields.html",tablename1=tablename1,table=table,pageTitle="Show Projects and Researchers based on field")
             #                      
        except Exception as e:
            print(e)
            return render_template("fields.html",pageTitle="Insert interesting Field",form = form)  
        
      
        
@app.route("/views",methods=["GET","POST"])
def getViews():
   
    form=MyForm()
    if request.method=="POST" and form.validate_on_submit():
        un = request.form['options']
        return redirect(url_for("getView1",option=un))
    else: 
        return render_template("views.html",pageTitle="Choose a View",form = form)      
                                                           
      
@app.route("/views/view<int:option>")
def getView1(option):
    
    try:
        if int(option)==1:
            tablename1="R_Projects View"
            cur = db.connection.cursor()
            cur.execute("CREATE VIEW r_projects AS  SELECT Researcher.researcher_name,  Researcher.researcher_lastname,  Researcher.researcher_id, Works_in.project_title  FROM   Researcher, Works_in  WHERE Researcher.researcher_id = Works_in.researcher_id")

            cur.execute("SELECT * FROM r_projects")
            column_names=[i[0] for i in cur.description]
        
            view1=[dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.execute("DROP VIEW r_projects")

            
           
            cur.close()
            return render_template("showview1.html",tablename1=tablename1,view1 = view1,pageTitle = "First View")
            
        elif int(option)==2:   
            tablename1="Overview_Project View"
            cur = db.connection.cursor()
            
            cur.execute("CREATE VIEW overview_project AS  SELECT Project.project_title, Project.budget,  Evaluation.evaluation_grade,Project.researcher_id  FROM Project, Evaluation   WHERE Project.evaluation_id=Evaluation.evaluation_id")

            cur.execute("SELECT * FROM overview_project")
            column_names=[i[0] for i in cur.description]
           
            view1=[dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.execute("DROP VIEW overview_project")

           
     
            cur.close()
            return render_template("showview2.html",tablename1=tablename1,view1 = view1,pageTitle = "Second View")
           
        
        
                                                            
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)
       
 
@app.route("/newfield", methods = ["GET", "POST"]) ## "GET" by default
def createfield():
    
    #Create new student in the database
    
    form = FieldForm()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newfield = form.__dict__
        field=newfield['field'].data
        
        query="INSERT INTO Research_Field (field_name) VALUES ('{}')".format(field)
     
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Field inserted successfully", "success")
            return redirect(url_for("index"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("newfield.html", pageTitle = "Create New Field", form = form)
    
@app.route("/allfields")
def getALLFIELDS():
       
        try:
           
            ## create connection to database
            cur = db.connection.cursor()
            ## execute query
            cur.execute("SELECT * FROM Research_Field")
            
            column_names = [i[0] for i in cur.description]
           
            table = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()

            return render_template("allfields.html",table=table,tablename1="Fields",pageTitle="Show all Research Fields")
                                   
        except Exception as e:
            print(e)
            return redirect(url_for("index"))               


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"),404

@app.errorhandler(500)
def server_error(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"),500