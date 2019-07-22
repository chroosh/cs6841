import time
from pwn import *

# to speed up network response time we're going to run this script
# within pwnable server
connection = remote('0', 9007)
