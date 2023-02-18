import subprocess
import os
import sys
from pathlib import Path

def capture(command):
    proc = subprocess.Popen(command,cwd='../cli', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out,err = proc.communicate()
    return out, err, proc.returncode
    
def test_healthcheck_json():
    command = [sys.executable,'healthcheck',"--format", "json"]
    out, err, exit_code= capture(command)
    assert b"200" in out
 
def test_resetall_json():  
    command = [sys.executable,'resetall',"--format", "json"]
    out, err, exit_code= capture(command)
    assert b"200" in out
    
def test_questionnaire_upd_json():
    command = [sys.executable, "questionnaire_upd", "--source", "../test/test_q.json","--format", "json"]
    out, err, exitcode = capture(command)
    assert b"200" in out
       
def test_resetq_json():
    command = [sys.executable, "resetq",  "--questionnaire_id", "QQ001","--format", "json"]
    out, err, exitcode = capture(command)
    assert b"200" in out
    

def test_healthcheck_csv():
    command = [sys.executable,'healthcheck',"--format", "csv" ]
    out, err, exit_code= capture(command)
    assert b"200" in out
 
def test_resetall_csv():  
    command = [sys.executable,'resetall',"--format", "csv" ]
    out, err, exit_code= capture(command)
    assert b"200" in out
    
def test_questionnaire_upd_csv():
    command = [sys.executable, "questionnaire_upd", "--source", '../test/test_q.json',"--format", "csv" ]
    out, err, exitcode = capture(command)
    assert b"200" in out
    
def test_resetq_csv():
    command = [sys.executable, "resetq",  "--questionnaire_id", 'QQ001',"--format", "csv" ]
    out, err, exitcode = capture(command)
    assert b"200" in out
        

