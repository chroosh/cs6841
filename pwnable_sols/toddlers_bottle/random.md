# random

^ = exclusive or - copies if bit is set in either operand but not both.
rand() is unseeded so therefore in theory it should generate the same number each time. You should
in theory should be able to find out what value that is through GDB.

Finally putting my x86 assembly skills into use. 
Setting a breakpoint where the random number is moved into $eax. 

Info registers doesn't actually print out the eax register for some reason but you can still print
out the register using:
p $eax

This gives a number 1804289383 which is the same number each time you run it - so you could in
theory, choose a number that XOR's with 1804289383 to give 0xdeadbeef.

To undo a XOR, simply XOR two other terms - so if we do 0x6B8B4567 (1804289383) ^ 0xdeadbeef,
we get 0xb526fb88. You can then pass in the decimal equivalent as 3039230856.


