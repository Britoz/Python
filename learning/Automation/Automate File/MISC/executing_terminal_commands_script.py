import subprocess
'''
Subprocess library allows Python script to interact with the command
line interface or shell
it contains many functions that can run terminal command

in this example, woking with 
Check call function
---
The perk of the check call function is it runs an executable in terminal
and waits until the process has finished before continuing our script
'''

for i in range(0, 5):
    # TODO: check call 5 times for example.py file
    try:
        subprocess.check_call(['python', 'example.py'])
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
