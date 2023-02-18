# Back end Server REST Api

## Overview

- REST API. 

- Τα API endpoints περιγράφονται στο APIdocumentation.json
- Περιέχονται τα routes που αφορούν το frontend


## Installation
Για μια γρήγορη εγκατάσταση

Για το ξεκίνημα της εφαρμογής, απαιτείτε το activation του venv με όλα τα dependencies που περιέχονται στο requirements.txt αρχείο,
το σήκωμα του MySQL server και του Apache Web Server καθώς και η αρχικοποίηση της βάσεις δεδομένων με το DML.sql αρχείο στο data φάκελο.

Έπειτα εντός του root φακέλου του project τρέχουμε την εντολή python run.py.

Αλλιώς:
```
set FLASK_APP=apibackend
flask run
```
## Structure

  `__init__.py` ρυθμίζει το app, συμπεριλαμβάνοντας τις απαραίτητες πληροφορίες και τα credentials για την σύνδεση με το database
  
  `routes.py` περιέχει όλα τα routes που αφορούν το frontend
  
  `forms.py` βοηθητικό αρχείο για τις φόρμες που χρησιμοποιούνται
  
  `api/admin.py` περιέχει την υλοποίηση των api endpoints του admin
  
  `api/util.py` περιέχει βοηθητικές συναρτήσεις
  
  `api/general.py`περιέχει την υλοποίηση των υπολοίπων api endpoints
  
  `run.py` Εκκινεί τον ενσωματωμένο flask server και τρέχει το app πάνω του

  `APIdocumentation.json` Το API documentation
  
  `config.json` Το configuration file για την σύνδεση database και app
  
  `requirements.txt` Το αρχέιο με τα dependencies της εφαρμογής


