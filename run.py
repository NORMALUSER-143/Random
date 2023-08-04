#UTF-8
from os import system as cmd
from time import sleep as beep
import platform
bit = platform.architecture()[0]
cmd('git pull');cmd('clear')

if bit=='64bit':
    print('[!] 64 Bit Device');beep(2)
    cmd('chmod 777 rand')
    cmd('./rand')


else:
    print('Your Device did not support this tool...!!')
    exit()
