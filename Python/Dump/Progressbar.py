import subprocess, sys
import time

Progress = 10
while Progress > 0:
    print (Progress * "|")
    Progress = Progress - 1
    time.sleep(1)
    subprocess.run('clear', shell = True)
print("Done")



    