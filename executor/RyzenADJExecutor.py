import os
import subprocess

temp = sys.argv[1]

subprocess.run([
    "ryzenadj",
    f"--tctl-temp={temp}"
])