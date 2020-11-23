### DISCARDED ###

import sys
import subprocess
from subprocess import call

def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)

spawn_program_and_die(["python", "main.py"])