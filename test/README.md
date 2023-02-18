# CLI TESTING

## Contents
- CLI functional tests

## Testing tool
- [pytest] - Full-featured Python testing tool

## Installation
Για γρήγορη εγκατάσταση:

Στο git bash terminal
```sh
python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt

```

## Testing
Χρήση μέσα στο test directory

Προυπόθεση αποτελεί η αρχικοποίηση της βάσης με το DML.sql

Test για τα endpoints του admin
```sh
pytest test_admin.py
```
Test για τα υπόλοιπα endpoints
```sh
pytest test_sessions.py
```
Βοηθητικά αρχεία για την διεξαγωγή των test
`bad.json`
`test_q.json`
  [pytest]: https://docs.pytest.org/en/stable/
