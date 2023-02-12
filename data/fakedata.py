import json
import random
import string

"""
with open('new.json', encoding='utf-8') as file:
    data=json.load(file)
Keywords=[]
L=[]
X=[]
Z=[]
myx=[]
myy=[]
texts=[]
x=0
y=0
booll=0
nextq=''

L.append("INSERT INTO Questionnaire (questionnaireID, questionnaire_Title, Aid) VALUES ('{}','{}',1);".format(data['questionnaireID'],data['questionnaireTitle']))
for keyword in data['keywords']:
    L.append("INSERT INTO Keywords (keyword) VALUES ('{}');".format(keyword))
    Z.append("INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('{}','{}');".format(data['questionnaireID'],keyword))
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
        print(qtext)
        for question in data['questions']:
            if question['qID ']==qtext[1]:
                texts.append(question['qtext'])
                for options in question['options']:
                    if options['optID']==qtext[0]:
                        texts.append(options['opttxt'])
        print(myx,myy)
        print(texts)
        strhelp='/'
        questiontext=questions['qtext'][0:myx[0]]+strhelp+texts[1]+strhelp+questions['qtext'][myy[0]+1:myx[1]] +strhelp+texts[0]+strhelp+questions['qtext'][myy[1]+1:]          
       
        L.append("INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('{}','{}','{}','{}','{}');".format(questions['qID '],questiontext,questions['required'],questions['type'],data['questionnaireID']))
    else:
        L.append("INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('{}','{}','{}','{}','{}');".format(questions['qID '],questions['qtext'],questions['required'],questions['type'],data['questionnaireID']))
    for option in questions['options']:
       X.append("INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('{}','{}');".format(option['optID'], option['opttxt']))
       if option['nextqID']=='-':
            nextq=questions['qID ']
       else:
            nextq=option['nextqID']
       Z.append("INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('{}','{}','{}');".format(questions['qID '], option['optID'], nextq))
"""
s = string.ascii_letters
for _ in range(10):
    c = ''.join(random.choice(s) for _ in range(8))
    

L=[]
Z=[]
with open('new9.json', encoding='utf-8') as f:
    data2=json.load(f)
    L.append("INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('{}','{}','{}');".format(data2['session'],data2['questionnaireID'],c))
    for answer in data2['answers']:
        Z.append("INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('{}','{}','{}');".format(answer['qID '],data2['session'],answer['ans']))

   
with open('DML2.sql', 'a') as file:
    for line in L:
        file.write(line)
        file.write('\n')
    #for line in X:
        #file.write(line)
        #file.write('\n')
    for line in Z:
        file.write(line)
        file.write('\n')
  