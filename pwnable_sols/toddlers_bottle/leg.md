# leg

Need to make key1, key2, key3 equal to key (0)

I was up at 5am writing this solution so I spent quite a bit thinking before I realised that this
was arm syntax, not intel and so some of the asm looked different.

The core idea was still the same you just need to find the return addresses of each of the keys
functions.

Looking at the disassembly for key 1:
This function returns the pc (program counter). In arm syntax, the program counter is equal to the
current instruction + 8 bytes. The current instruction woul d be 0x00008cdc. + 8 would be
0x00008ce4

Looking at the disassembly for key 2:
The function contains a bx r6. CPU is now in 16 bit mode where values of PC are + 4 instead of + 8
The current instruction would be 0x00008d04, the PC would be +4 0x00008d08 and adding +4 on top
would make it 0x00008d0c

Looking at the disassembly for key 3:
lr is the link register, essentially the ($ra). Looking back into the main funciton, the value of
lr is 0x00008d80

Adding all of these up, converting it into a decimal will give you the flag.
