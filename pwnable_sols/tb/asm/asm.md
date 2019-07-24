# asm

From what I've read, you just need to write some shellcode and 
run it from within the asm binary.

Shellcode is typically machine code / or assembly code that is
used to generate a shell.

In this case, I implemented x64 assembly for 3 syscalls:

open()
read()
write()

Looking at the documentation for x64 asm (system call table)
made implementing the syscalls easier.
