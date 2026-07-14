# Libraries
import subprocess as sp
import os

def set_values(temp):
    user_shell = os.environ.get("SHELL", "/bin/sh")
    try:
        cmd = ["pkexec", user_shell, '-c', f"ryzenadj --tctl-temp={temp}"]
        res = sp.run(cmd, capture_output=True, text=True, check=True)
        print("Output:", res.stdout.strip())
    except sp.CalledProcessError as e:
        print("Auth failed:", e)

set_values(74)