from pwn import *

p = process("/home/fsb/fsb", stdout=open('/dev/null', 'w+'))

