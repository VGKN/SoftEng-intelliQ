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
    assert b"200" in out
