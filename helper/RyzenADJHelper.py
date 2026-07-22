# Libraries
import subprocess as sp
import os

def set_values(temp):
  
    helper = os.path.join(
        os.path.dirname(__file__),
        "../helper/ryzen-helper.py"
    )

    subprocess.run([
        "pkexec",
        "python",
        helper,
        temp
    ])