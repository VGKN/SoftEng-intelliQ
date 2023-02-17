import subprocess
import os
import sys
from pathlib import Path


def capture(command):
    proc = subprocess.Popen(command,cwd="../cli", stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out,err = proc.communicate()
    return out, err, proc.returncode
    
def test_questionnaire():
    command = [sys.executable,"questionnaire","--questionnaire_id", "QQ000"]
    out, err, exitcode = capture(command)
    assert b"200" in out

def test_question():
    command = [sys.executable,"question", "--questionnaire_id", "QQ000" ,"--question_id", "Q01"]
    out, err, exitcode = capture(command)
    assert b"200" in out
    
def test_doanswer():
    command = [sys.executable,"doanswer","--questionnaire_id", "QQ000", "--question_id", "Q01", "--session_id", "AZaz", "--option_id", "Q01A1"]
    out, err, exitcode = capture(command)
    assert b"200" in out

def test_getsessionanswers():
    command = [sys.executable,"getsessionanswers", "--questionnaire_id", "QQ000" ,"--session_id", "ATBA"]
    out, err, exitcode = capture(command)
    assert b"200" in out
    
def test_getquestionanswers():
    command = [sys.executable,"getquestionanswers" ,"--questionnaire_id", "QQ000" ,"--question_id", "Q01"]
    out, err, exitcode = capture(command)
    assert b"200" in out  
