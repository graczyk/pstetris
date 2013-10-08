import os
import psutil

PROCNAME = "Preview"

print('Welcome to postscript tetris. Depends on Preview.app on OS X for now')

os.system('open -a Preview test.ps')

print('we will now test updating the PS file in the background')
raw_input("Press Enter to continue...")

str = open('test.ps','r').read()
str += "72 600 moveto (Hell0 w0rld!) show showpage"
open('test.ps','w').write(str)

#from http://stackoverflow.com/questions/2940858/kill-process-by-name-in-python
for proc in psutil.process_iter():
    if proc.name == PROCNAME:
        proc.kill()
#this doesn't solve the problem of having to close that window first because of shitty application behavior on OS X
os.system('open -g -a Preview test.ps')
