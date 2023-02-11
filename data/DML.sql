DELETE FROM Admin;
DELETE FROM Questionnaire;
DELETE FROM Sesion;
DELETE FROM Keywords;
DELETE FROM Question;
DELETE FROM Questionnaire_Keywords;
DELETE FROM Options;
DELETE FROM Session_Questions_Options;
DELETE FROM Questions_Options;


INSERT INTO Admin (Aid, Last_name, First_name, Telephone) VALUES (1,'Tiz', 'Ali', 6944343432);

INSERT INTO Questionnaire (questionnaireID, questionnaireTitle, Aid) VALUES ('QQ000','My first research questionnaire',1);

INSERT INTO Keywords (keyword) VALUES ('footbal');
INSERT INTO Keywords (keyword) VALUES ('islands');
INSERT INTO Keywords (keyword) VALUES ('timezone');

INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('P00','���� ����� �� mail ���;','FALSE','profile','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('P01','���� ����� � ������ ���;','TRUE','profile','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q01','���� ����� �� ��������� ��� �����;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q02','���������� �� �� ����������;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q03','�� ����� �����;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q04','����� ����� �� ����;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q05','�� �������� ��� ���������� /���/ ���� ������� /����� ����� �� ����;/: ���� � ����� ��� �� �� �������� ���;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q06','����� ���������� ����������','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q07','������ ��������� ���;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q08','���������� �� ������� � ��� ���� �����;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q09','�� �������� ��� ���������� /���/ ���� ������� /���������� �� ������� � ��� ���� �����;/: ��������� �� ������ � ��� ��������� ���;','TRUE','question','QQ000');

INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ATBP','QQ000','vUbGKTIr');

INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P00TXT','<open string>');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A1','<30');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A2','30-50');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A3','50-70');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A4','>70');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01A1','�������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01A2','�������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01A3','�������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q02A1','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q02A2','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03A1','������������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03A2','���������� ');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03A3','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q04A1','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q04A2','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05A1','�����');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05A2','�����');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05A3','������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q06A1','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q06A2','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07A1','������ - �������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07A2','������������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07A3','�������');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q08A1','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q08A2','���');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q09A1','������');

INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q09A2','���������');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ000','footbal');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ000','islands');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ000','timezone');

INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P00','P00TXT','P01')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A1','Q01')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A2','Q01')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A3','Q01')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A4','Q01')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01','Q01A1','Q02')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01','Q01A2','Q02')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01','Q01A3','Q02')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q02','Q02A1','Q03')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q02','Q02A2','Q04')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03','Q03A1','Q04')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03','Q03A2','Q04')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03','Q03A3','Q04')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q04','Q04A1','Q05')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q04','Q04A2','Q06')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05','Q05A1','Q07')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05','Q05A2','Q07')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05','Q05A3','Q07')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q06','Q06A1','Q07')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q06','Q06A2','Q07')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07','Q07A1','Q08')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07','Q07A2','Q08')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07','Q07A3','Q08')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q08','Q08A1','Q09')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q08','Q08A2','-')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q09','Q09A1','-')
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q09','Q09A2','-')

INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P00','ATBP','<*>');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01','ATBP','P01A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01','ATBP','Q01A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02','ATBP','Q02A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03','ATBP','Q03A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04','ATBP','Q04A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q05','ATBP','Q05A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q06','ATBP','Q06A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q07','ATBP','Q07A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08','ATBP','Q08A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q09','ATBP','Q09A2');
