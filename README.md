# Software Engineering Project 2022-2023

**Semester Project for Software Engineering course @ NTUA, 7th Semester 2022-2023**

Team Name: SoftEng22-19

Project Name: intelliQ

This project was conducted for the course of Software Engineering at the 2022-2023 Winter semester of the Electrical and Computer Engineering School at the National Technical University of Athens


Scenario

The subject of the project is the development of a software application for the configuration and
running  of "intelligent questionnaires", which will be called "intelliQ". The intelliQ app will
used to aggregate data from such questionnaires in various surveys.


Technical Details

| Asset | Technologies Used |
| ----- | ----------- |
| backend | Python Flask |
| frontend | html, css, bootstrap5 |
| database | MySQL |
| CLI | Python3 argparse |


**The project is a collaborate effort of a team of 4 members:**


| Name | Registration Number
| ----- | -----
| Theos Stefanos | 03119219
| Bitsanis Athanasios | 03119136
| Kassaris Nikolaos | 03119188
| Vougias Konstantinos | 03119144

## Flask Backend
`cd apibackend/`
 
### Installation
 ```Σε περιβάλλον cmd
 python -m venv venv
 cd venv/Scripts
 activate
 cd..
 cd..
 pip install -r requirements.txt
 ```
 
### DB

Χρησιμοποιούμε XAMPP και συνδεόμαστε στον Apache Web Server στο Port:80 και τρέχομε MySQL Server στο Port:3306.
 
#### Κάθε επόμενη φορά
Σηκωνουμε τα services: Ανοιγουμε XAMPP και ανοιγουμε Apache Web Server και MySQL Server.
Ανοιγω terminal στον φακελο Scripts του venv. 
```
activate
cd..
cd..
python run.py
```
### DBMS
Χρησιμοποιουμε MySQL Server χωρις χρηση ORM. 

### Configurations

To configuration για τα credentials της βασης δεδομενων βρισκονται στο αρχειο config.json μεσα στο github για την επιδειξη της εφαρμογης.

### Run
Εκτελω την παρακατω εντολη στο terminal με ανεβασμενα τα services και activated το venv:

```python run.py```

Για δοκιμή του Rest API methods χρησιμοποιoυμε το Postman.



 
 
 


