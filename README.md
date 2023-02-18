# Software Engineering Project 2022-2023

**Εξαμηνιαίο Project για το μάθημα "Τεχνολογία Λογισμικού" @ NTUA, 7ο Εξάμηνο 2022-2023**

Όνομα ομάδας: SoftEng22-19

Όνομα Project: intelliQ


Το project αυτό διεξήχθη για το μάθημα "Τεχνολογία Λογισμικού" στο χειμερινό εξάμηνο της χρονιάς 2022-2023 της σχολής Ηλεκτρολόγων Μηχανικών και Μηχανικών Υπολογιστών.



## Στόχος project

Ο στόχος του project αυτού είναι η ανάπτυξη μιας εφαρμογής λογισμικού για την διομόρφωση και την διεξαγωγή "έξυπνων ερωτηματολογίων", η οποία ονομάζεται "intelliQ". Η εφαρμογή "intelliQ" θα χρησιμοποιηθεί για την άντληση δεδομένων από τα ερωτηματολόγια αυτά και την διοχέτευση τους σε διάφορες έρευνες.



**Τεχνικές Λεπτομέρειες** 

| Asset | Technologies Used |
| ----- | ----------- |
| backend | Python Flask |
| frontend | html, css, bootstrap5 |
| database | MySQL |
| CLI | Python3 argparse |



**Το project είναι μια συλλογική προσπάθεια μιας ομάδας 4 ατόμων:** 


| Ονοματεπώνυμο | Αριθμός Μητρώου
| ----- | -----
| Θέος Στέφανος | 03119219
| Μπιτσάνης Αθανάσιος | 03119136
| Κάσσαρης Νικόλαος | 03119188
| Βούγιας Κωνσταντίνος | 03119144

## Εξαρτήσεις

 - [XAMPP](https://www.apachefriends.org/download.html) για Windows
 - [Python],(https://www.python.org/downloads/) με τις επιπρόσθετες βιβλιοθήκες:
    - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)
    - [Flask-WTForms](https://flask-wtf.readthedocs.io/en/1.0.x/)

Για το backend χρησιμοποιoυμε το Flask Framework της Python.

Χρησιμοποιoύμε το pip(python's package manager) για να κατεβάσουμε κάθε πακέτο της Python κατευθείαν για όλο το σύστημα, ή δημιουργούμε ενα virtual environment με το [`venv`] module.
Τα αναγκαία πακέτα για αυτήν την εφαρμογή ειναι καταγεγραμμένα στο `requirements.txt` και μπορούν να 'κατεβαστούν' όλα μαζί με την εντολή: `pip install -r requirements.txt`.

Για να γίνει αποστολή "queries" σε μια Βάση Δεδομένων από ένα πρόγραμμα σε Python, πρέπει να εγκατασταθεί μία σύνδεση μεταξύ του προγράμματος και του server της Βάσης Δεδομένων. Αυτό επιτυγχάνεται από ένα αντικείμενο "cursor" από την βιβλιοθήκη "Flask-MySQLdb", χρησιμοποιώντας τις κατάλληλες μεθόδους ("execute", "commit").

## Flask Backend
`cd apibackend/`
 
## Installation
 Σε περιβάλλον cmd
 ```
 python -m venv venv
 cd venv/Scripts
 activate
 cd..
 cd..
 pip install -r requirements.txt
```
 
## DB
Χρησιμοποιούμε XAMPP και συνδεόμαστε στον Apache Web Server στο Port:80 και τρέχουμε MySQL Server στο Port:3306.
 
## Κάθε επόμενη φορά
Σηκώνουμε τα services: Ανοίγουμε XAMPP και ανοίγουμε Apache Web Server και MySQL Server.
Ανοίγω terminal στον φάκελο Scripts του venv. 
```
activate
cd..
cd..
python run.py
```
## DBMS
Χρησιμοποιούμε MySQL Server χωρίς χρήση ORM. 

## Configurations

To configuration για τα credentials της βάσης δεδομένων βρίσκονται στο αρχείο config.json.

Δεν συνίσταται να ανεβάζετε κωδικούς πρόσβασης ή API κλειδιά στο github. Εμείς ανεβάσαμε το αρχείο config.json για την επίδειξη της εφαρμογής. Κανονικά θα συμπεριλαμβανόταν στο .gitignore:
Κάνουμε import τα credentials στο `__init__.py` αντικαθιστώντας την `app.config` εντολή με:
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

## Run
Εκτελώ την παρακάτω εντολή στο terminal με ανεβασμένα τα services και activated το venv:

```python run.py```

Για δοκιμή του Rest API methods χρησιμοποιούμε το Postman.
