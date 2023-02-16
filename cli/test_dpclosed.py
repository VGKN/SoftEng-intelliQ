import subprocess
import os
import sys
from pathlib import Path

def capture(command):
    proc = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out,err = proc.communicate()
    return out, err, proc.returncode
    
def test_healthcheck():
    command = [sys.executable,'healthcheck']
    out, err, exit_code= capture(command)
    assert b"500" in out

def test_doanswer():
    pass
    
def test_questionnaire():
    pass
    
def test_question():
    pass
    
def test_questionnaire_upd():
    pass
    
def test_resetall():  
	command = [sys.executable,'resetall']
    out, err, exit_code= capture(command)
    assert b"500" in out:
    
def test_resetq():
    pass
    
def test_getquestionanswers():
    pass
 
def test_getsessionanswers():
    pass