import subprocess
import os
import sys
from pathlib import Path

def capture(command):
    proc = subprocess.Popen(command,cwd="../cli", stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out,err = proc.communicate()
    return out, err, proc.returncode
    
    
def test_questionnaire_json():
    command = [sys.executable,"questionnaire","--questionnaire_id", "QQ000","--format", "json" ]
    out, err, exitcode = capture(command)
    assert b"200" in out

def test_question_json():
    command = [sys.executable,"question", "--questionnaire_id", "QQ000" ,"--question_id", "Q01","--format", "json" ]
    out, err, exitcode = capture(command)
    assert b"200" in out
    
def test_doanswer_json():
    command = [sys.executable,"doanswer","--questionnaire_id", "QQ000", "--question_id", "Q01", "--session_id", "AAZZ", "--option_id", "Q01A1","--format", "json" ]
    out, err, exitcode = capture(command)
    assert b"200" in out

def test_getsessionanswers_json():
    command = [sys.executable,"getsessionanswers", "--questionnaire_id", "QQ000" ,"--session_id", "ATBA","--format", "json" ]
    out, err, exitcode = capture(command)
    assert b"200" in out
    
def test_getquestionanswers_json():
    command = [sys.executable,"getquestionanswers" ,"--questionnaire_id", "QQ000" ,"--question_id", "Q01","--format", "json" ]
    out, err, exitcode = capture(command)
    assert b"200" in out  
    
    
    
def test_questionnaire_csv():
    command = [sys.executable,"questionnaire","--questionnaire_id", "QQ000","--format", "csv" ]
    out, err, exitcode = capture(command)
    assert b"200" in out

def test_question_csv():
    command = [sys.executable,"question", "--questionnaire_id", "QQ000" ,"--question_id", "Q01","--format", "csv" ]
    out, err, exitcode = capture(command)
    assert b"200" in out
    
def test_doanswer_csv():
    command = [sys.executable,"doanswer","--questionnaire_id", "QQ000", "--question_id", "Q01", "--session_id", "AAZA", "--option_id", "Q01A1","--format", "csv" ]
    out, err, exitcode = capture(command)
    assert b"200" in out

def test_getsessionanswers_csv():
    command = [sys.executable,"getsessionanswers", "--questionnaire_id", "QQ000" ,"--session_id", "ATBA","--format", "csv" ]
    out, err, exitcode = capture(command)
    assert b"200" in out
    
def test_getquestionanswers_csv():
    command = [sys.executable,"getquestionanswers" ,"--questionnaire_id", "QQ000" ,"--question_id", "Q01","--format", "csv" ]
    out, err, exitcode = capture(command)
    assert b"200" in out  