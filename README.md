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

### Dependencies

 - [MySQL] for Windows
 - [Python], with the additional libraries:
    - [Flask]
    - [Flask-MySQLdb]
    - [Flask-WTForms]

Για το backend χρησιμοποιoυμε το Flask Framework της Python.

Χρησιμοποιoυμε το pip(python's package manager) για να κατεβασουμε καθε πακετο της Python κατευθειαν για ολο το συστημα, η δημιουργουμε ενα virtual environment με το [`venv`] module.
Τα αναγκαια πακετα για αυτην την εφαρμογη ειναι καταγεγραμμενα στο `requirements.txt` και μπορουν να 'κατεβαστουν' ολα μαζι με την εντολη: `pip install -r requirements.txt`.

In order to send queries to a database from a Python program, a connection between it and the databases' server must be established first. That is accomplished by a cursor object from the `Flask-MySQLdb` library, and using the appropriate methods (`execute`, `commit`)

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

To configuration για τα credentials της βασης δεδομενων βρισκονται στο αρχειο config.json.

Δεν συνισταται να ανεβαζετε κωδικους προσβασης η API κλειδια στο github.Εμεις ανεβασαμε το αρχειο config.json για την επιδειξη της εφαρμογης.Κανονικα θα συμπεριλαμβανοταν στο .gitignore:
 Κανουμε import τα credentials στο `__init__.py` αντικαθιστοντας την `app.config` εντολη με:
    _apibackend/config.json_
    ```json
    {
        "MYSQL_USER": "root",
        "MYSQL_PASSWORD": "",
        "MYSQL_DB": "intelliQ",
        "MYSQL_HOST": "localhost",
        "SECRET_KEY": "key",
        "WTF_CSRF_SECRET_KEY": "key"
    }
    ```
   
    ```python
    import json
    ## ...
    app.config.from_file("config.json", load = json.load)
    ```

### Run
Εκτελω την παρακατω εντολη στο terminal με ανεβασμενα τα services και activated το venv:

```python run.py```

Για δοκιμή του Rest API methods χρησιμοποιoυμε το Postman.
