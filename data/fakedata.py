import json

with open('new.json', encoding='utf-8') as file:
    print("hi")
    data=json.load(file)
Keywords=[]
L=[]
X=[]
#print(data['questionnaireID'])
L.append("INSERT INTO Questionnaire (questionnaireID, questionnaireTitle, Aid) VALUES ('{}','{}',1);".format(data['questionnaireID'],data['questionnaireTitle']))
for keyword in data['keywords']:
    L.append("INSERT INTO Keywords (keyword) VALUES ('{}');".format(keyword))
for questions in data['questions']:
    x=questions['qtext'].find("[*")
    y=questions['qID ']
    L.append("INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('{}','{}','{}','{}','{}');".format(questions['qID '],questions['qtext'],questions['required'],questions['type'],data['questionnaireID']))
    print(x)
    for option in questions['options']:
       X.append("INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('{}','{}');".format(option['optID'], option['opttxt']))
   #Keywords.append(keywords)

#print(L)
#print(X)
"""with open('DML.sql', 'a') as file:
    for line in L:
        file.write(line)
        file.write('\n')
    for line in X:
        file.write(line)
        file.write('\n')
    """