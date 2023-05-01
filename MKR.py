#coding=utf-8
import os, sys, time
A = '\x1b[1;91m'
print(f'{A} good luck \n GG \n KURDISH 21 ')

import platform
os.system('xdg-open https://crackbdofficial.blogspot.com')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Mkr.so Mkr32.so')
except:
    pass
os.system('rm -rf Mkr.so Mkr64.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Mkr64.so'):                                                                                                                          
        os.system('curl -L https://github.com/SHA3A9')
        import Mkr64
    else:
        import Mkr64
elif bit == '32bit':
    if not os.path.isfile('Mkr32.so'):
        os.system('curl -L https://github.com/SHA3A9')
        import Mkr32
    else:
        import Mkr32
