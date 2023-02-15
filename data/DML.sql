DELETE FROM Questionnaire_Keywords;
DELETE FROM Questions_Options;
DELETE FROM Session_Questions_Options;
DELETE FROM Question;
DELETE FROM Sesion;
DELETE FROM Questionnaire;
DELETE FROM Admin;
DELETE FROM Keywords;
DELETE FROM Options;
DELETE FROM User;


INSERT INTO Admin (Aid, Last_name, First_name, Telephone) VALUES (1,'Tiz', 'Ali', 6944343432);
INSERT INTO Questionnaire (questionnaireID, questionnaire_Title, Aid) VALUES ('QQ001','Thoughts on Formula 1 Racing',1);
INSERT INTO Keywords (keyword) VALUES ('motorsports');
INSERT INTO Keywords (keyword) VALUES ('driving');
INSERT INTO Keywords (keyword) VALUES ('celebrities');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('P01a','Ποια είναι η ηλικία σας;','TRUE','profile','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q01a','Ασχολείστε με τις εξέλιξεις στο πρωτάθλημα της Formula 1 ;','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q02a','Πόσα χρόνια είστε φάν της Formula 1;','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q03a','Υποστηρίζετε κάποια απο τις 3 κυριάρχες ομάδες','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q04a','Δεδομένου πως απαντήσατε \'Ναι την Mercedes\' στην ερώτηση \'Υποστηρίζετε κάποια απο τις 3 κυριάρχες ομάδες\': Ποιον απο τους δύο οδηγούς της Mercedes υποστηρίζετε περισσότερο;','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q05a','Δεδομένου πως απαντήσατε \'Ναι την Ferrari\' στην ερώτηση \'Υποστηρίζετε κάποια απο τις 3 κυριάρχες ομάδες\': Ποιός απο τους δύο οδηγούς της Ferrari θεωρείτε πως είναι χειρότερος','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q06a','Με δεδομένο ότι απαντήσατε \'Ναι την Red Bull Racing\' στην ερώτηση \'Υποστηρίζετε κάποια απο τις 3 κυριάρχες ομάδες\': Ποιός απο τους δύο οδηγούς της Red Bull Racing θεωρείτε πως είναι καλύτερος','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q07a','Με δεδομένο ότι απαντήσατε \'Όχι, καμία\' στην ερώτηση \'Υποστηρίζετε κάποια απο τις 3 κυριάρχες ομάδες\': Ήσασταν κάποτε φαν κάποιας απο τις 3 κυρίαρχες ομάδες;','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q08a','Ποιοί αγώνες θα λέγατε οτί είναι πιο ενδιαφέροντες στο πρωτάθλημα','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q09a','θα παρακολουθούσατε κάποιον αγώνα εάν σας το πρότεινε κάποιος φίλος σας;','TRUE','question','QQ001');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q10a','Συγκρίνοντας με τον περίγυρο σας, νίωθετε πως η δημοφιλία του αθλήμτος έχει ανέβει;','TRUE','question','QQ001');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01aA1','<20');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01aA2','20-40');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01aA3','40-50');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01aA4','>50');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01aA1','Ναι είμαι φαν του αθλήματος');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01aA2','Όχι ιδιαίτερα');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q02aA1','Λιγότερο απο 1 χρόνο');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q02aA2','2-5 Χρόνια');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q02aA3','Πάνω απο 5 Χρόνια');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03aA1','Ναι την Mercedes');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03aA2','Ναι την Ferrari');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03aA3','Ναι την Red Bull Racing');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03aA4','Όχι, καμία');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q04aA1','Louis Hamilton');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q04aA2','George Russell');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05aA1','Charles LeClerc');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05aA2','Carlos Sainz');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q06aA1','Max Verstappen');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q06aA2','Perez');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07aA1','Παλιότερα Ναι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07aA2','Ποτέ');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q08aA1','Αγώνας Πόλης');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q08aA2','Αγώνας Πίστας');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q09aA1','Αποκλείεται');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q09aA2','Θα το σκεφτόμουν');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q10aA1','Ναι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q10aA2','Ίσως');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q10aA3','Οχι');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ001','motorsports');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ001','driving');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ001','celebrities');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01a','P01aA1','Q01a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01a','P01aA2','Q01a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01a','P01aA3','Q01a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01a','P01aA4','Q01a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01a','Q01aA1','Q02a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01a','Q01aA2','Q09a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q02a','Q02aA1','Q03a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q02a','Q02aA2','Q03a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q02a','Q02aA3','Q03a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03a','Q03aA1','Q04a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03a','Q03aA2','Q05a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03a','Q03aA3','Q06a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03a','Q03aA4','Q07a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q04a','Q04aA1','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q04a','Q04aA2','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05a','Q05aA1','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05a','Q05aA2','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q06a','Q06aA1','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q06a','Q06aA2','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07a','Q07aA1','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07a','Q07aA2','Q08a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q08a','Q08aA1','Q10a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q08a','Q08aA2','Q10a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q09a','Q09aA1','Q10a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q09a','Q09aA2','Q10a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q10a','Q10aA1','Q10a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q10a','Q10aA2','Q10a');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q10a','Q10aA3','Q10a');

INSERT INTO Questionnaire (questionnaireID, questionnaire_Title, Aid) VALUES ('QQ000','My first research questionnaire',1);
INSERT INTO Keywords (keyword) VALUES ('footbal');
INSERT INTO Keywords (keyword) VALUES ('islands');
INSERT INTO Keywords (keyword) VALUES ('timezone');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('P01','Ποια είναι η ηλικία σας;','TRUE','profile','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q01','Ποιο είναι το αγαπημένο σας χρώμα;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q02','Ασχολείστε με το ποδόσφαιρο;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q03','Τι ομάδα είστε;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q04','Έχετε ζήσει σε νησί;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q05','Με δεδομένο ότι απαντήσατε \'Ναι\' στην ερώτηση \'Έχετε ζήσει σε νησί;\': Ποια η σχέση σας με το θαλάσσιο σκι;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q06','Είστε χειμερινός κολυμβητής','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q07','Κάνετε χειμερινό σκι;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q08','Συμφωνείτε να αλλάζει η ώρα κάθε χρόνο;','TRUE','question','QQ000');
INSERT INTO Question (Question_ID, Qtext, Qrequired, Qtype, QuestionaireID) VALUES ('Q09','Με δεδομένο ότι απαντήσατε \'Οχι\' στην ερώτηση \'Συμφωνείτε να αλλάζει η ώρα κάθε χρόνο;\': Προτιμάτε τη θερινή ή την χειμερινή ώρα;','TRUE','question','QQ000');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A1','<30');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A2','30-50');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A3','50-70');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('P01A4','>70');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01A1','Πράσινο');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01A2','Κόκκινο');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q01A3','Κίτρινο');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q02A1','Ναι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q02A2','Οχι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03A1','Παναθηναϊκός');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03A2','Ολυμπιακός ');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q03A3','ΑΕΚ');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q04A1','Ναι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q04A2','Οχι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05A1','Καμία');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05A2','Μικρή');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q05A3','Μεγάλη');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q06A1','Ναι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q06A2','Οχι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07A1','Σπάνια - καθόλου');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07A2','Περιστασιακά');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q07A3','Τακτικά');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q08A1','Ναι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q08A2','Οχι');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q09A1','Θερινή');
INSERT INTO Options (Opt_ID, Opt_Text) VALUES ('Q09A2','Χειμερινή');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ000','footbal');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ000','islands');
INSERT INTO Questionnaire_Keywords (QuestionnaireQuestionnaireID, KeywordsKeyword) VALUES ('QQ000','timezone');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A1','Q01');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A2','Q01');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A3','Q01');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('P01','P01A4','Q01');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01','Q01A1','Q02');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01','Q01A2','Q02');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q01','Q01A3','Q02');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q02','Q02A1','Q03');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q02','Q02A2','Q04');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03','Q03A1','Q04');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03','Q03A2','Q04');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q03','Q03A3','Q04');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q04','Q04A1','Q05');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q04','Q04A2','Q06');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05','Q05A1','Q07');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05','Q05A2','Q07');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q05','Q05A3','Q07');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q06','Q06A1','Q07');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q06','Q06A2','Q07');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07','Q07A1','Q08');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07','Q07A2','Q08');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q07','Q07A3','Q08');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q08','Q08A1','Q09');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q08','Q08A2','Q08');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q09','Q09A1','Q09');
INSERT INTO Questions_Options (QuestionID, OptID, Next_Q) VALUES ('Q09','Q09A2','Q09');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATB','QQ001','ffOAEqPp');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATB','P01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATB','Q01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02a','ZATB','Q02aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03a','ZATB','Q03aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q05a','ZATB','Q05aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08a','ZATB','Q08aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATB','Q10aA2');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATA','QQ001','RGVPKGjb');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATA','P01aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATA','Q01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02a','ZATA','Q02aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03a','ZATA','Q03aA3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q06a','ZATA','Q06aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08a','ZATA','Q08aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATA','Q10aA3');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATC','QQ001','lHEfmDbd');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATC','P01aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATC','Q01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02a','ZATC','Q02aA3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03a','ZATC','Q03aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04a','ZATC','Q04aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08a','ZATC','Q08aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATC','Q10aA2');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATD','QQ001','QSAesiYi');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATD','P01aA3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATD','Q01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02a','ZATD','Q02aA3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03a','ZATD','Q03aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q05a','ZATD','Q05aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08a','ZATD','Q08aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATD','Q10aA1');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATE','QQ001','xCTCpXRg');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATE','P01aA4');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATE','Q01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02a','ZATE','Q02aA3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03a','ZATE','Q03aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04a','ZATE','Q04aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08a','ZATE','Q08aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATE','Q10aA1');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATF','QQ001','jhOsOaEH');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATF','P01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATF','Q01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02a','ZATF','Q02aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03a','ZATF','Q03aA3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q06a','ZATF','Q06aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08a','ZATF','Q08aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATF','Q10aA1');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATG','QQ001','VyEcIAZg');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATG','P01aA4');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATG','Q01aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q09a','ZATG','Q09aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATG','Q10aA3');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATH','QQ001','KsPQEfJv');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATH','P01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATH','Q01aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q09a','ZATH','Q09aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATH','Q10aA1');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ZATI','QQ001','CiOFCJJn');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01a','ZATI','P01aA4');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01a','ZATI','Q01aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02a','ZATI','Q02aA2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03a','ZATI','Q03aA4');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q07a','ZATI','Q07aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08a','ZATI','Q08aA1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q10a','ZATI','Q10aA2');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ATBP','QQ000','BJZxasfT');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01','ATBP','P01A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01','ATBP','Q01A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02','ATBP','Q02A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03','ATBP','Q03A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04','ATBP','Q04A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q05','ATBP','Q05A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q07','ATBP','Q07A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08','ATBP','Q08A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q09','ATBP','Q09A1');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ATBA','QQ000','DeGXGcoa');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01','ATBA','P01A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01','ATBA','Q01A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02','ATBA','Q02A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03','ATBA','Q03A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04','ATBA','Q04A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q06','ATBA','Q06A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q07','ATBA','Q07A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08','ATBA','Q08A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q09','ATBA','Q09A2');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ATBB','QQ000','dhtiUhHy');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01','ATBB','P01A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01','ATBB','Q01A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02','ATBB','Q02A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03','ATBB','Q03A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04','ATBB','Q04A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q05','ATBB','Q05A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q07','ATBB','Q07A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08','ATBB','Q08A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q09','ATBB','Q09A2');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ATBC','QQ000','wPtzzwAw');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01','ATBC','P01A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01','ATBC','Q01A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02','ATBC','Q02A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04','ATBC','Q04A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q05','ATBC','Q05A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q07','ATBC','Q07A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08','ATBC','Q08A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q09','ATBC','Q09A1');
INSERT INTO Sesion (Session_ID, QuestionnaireID, UserString) VALUES ('ATBD','QQ000','UdiCHnEz');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('P01','ATBD','P01A4');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q01','ATBD','Q01A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q02','ATBD','Q02A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q03','ATBD','Q03A1');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q04','ATBD','Q04A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q06','ATBD','Q06A2');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q07','ATBD','Q07A3');
INSERT INTO Session_Questions_Options (Q_ID, S_ID, O_ID) VALUES ('Q08','ATBD','Q08A2');
