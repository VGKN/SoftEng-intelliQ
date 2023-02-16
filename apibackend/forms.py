from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email

## when passed as a parameter to a template, an object of this class will be rendered as a regular HTML form
## with the additional restrictions specified for each field

class MyForm(FlaskForm):

    submit = SubmitField("Submit")
    
class FieldForm(FlaskForm):

    field=StringField(label="Field",validators=[DataRequired(message = "Field is required to proceed")])
    
    submit = SubmitField("Submit")
    
class ProjectForm(FlaskForm):

    admin_username=StringField(label="Admin Username")
    admin_password=StringField(label="Admin Password")
    submit = SubmitField("Submit")

class QuestionForm(FlaskForm):
    q_keyword=StringField(label="Question Keyword")
    submit = SubmitField("Submit")
    
    