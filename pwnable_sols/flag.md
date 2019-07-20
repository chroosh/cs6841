# flag

Binary exercise. I immediately tried to run the binary file which gave me the string:

"I will malloc() the string and strcpy the string there. Take it."

Just a thought - this must mean the string is stored on the heap, since it was dynamically
allocated.

I ran the binary through GDB and tried to disassemble main, but it would show that no symbol was
loaded.

I also opened the file in Binja and had a look at the assembly. There were some values like
0xffffffffffffffff and 0xfffffffffffffffc neither which are the flag.

Here is where the help begins.

When running "strings -20 flag" it generates a couple lines stating that the file was packed with
the UPX executable packer, which compresses binaries and decompresses them at runtime.

You can decompress the binary through:
- sudo apt install upx-ucl
- upx -d flag

Decompressing the binary allowed me to run it in GDB and disassemble the main function. Within 
the disassembled code there was a comment with the flag address.

You could then just run the command:
x/s *ptr

x in GDB displays the memory contents at a given address using a specified format - here which is
s : string, the flag.

