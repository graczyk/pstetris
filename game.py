import os, subprocess

print('Welcome to postscript tetris.')

p = subprocess.Popen("gv -watch -spartan test.ps", shell=True)
if p < 0:
    print('things went wrong')

print('we will now test updating the PS file in the background')
raw_input("Press Enter to continue...")

str = '%! 
 newpath 
 1.5 setlinewidth 
 65 65 moveto 
 65 0 rlineto
 0 65 rlineto 
 -65 0 rlineto 
 closepath
 stroke
 showpage'
open('test.ps','w').write(str)


raw_input("Press Enter to continue...")

p.terminate()
