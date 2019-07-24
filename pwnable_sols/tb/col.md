# col

Had to look at a solution off youtube for this one. I've never worked with hex at a binary level
before and have limited knowledge of hashing algorithms. 

My approach involved copying the file off the pwnable server to actually debug how the binary 
worked. I was able to figure out that the hashing function converted the input into 5 x 4 int
chunks that were added up and that was the hashcode.

I was lost after that - I tried a variety of different combinations like 20 x 1 and 20 x 0 and
20 x 'a' etc. Somehow the idea of division never occured to me.

Learnt how to use GDB to disassemble programs into x86 asm.
* set disassembly-flavor intel
* disass [symbol]
* break *(addr)
* r (input)
* info r => gives information about the registers`

## Solution Writeup

This challenge asks for a 20 byte input which generates a hashcode using a simple algorithm that
type casts the input into an int pointer - essentially splitting the input into 5 x 4 byte parts
(because the size of an int is 4 bytes).

The for loop reads all 5 parts of the input and sums it up to generate a hashcode. We need to 
input 20 bytes of characters such that when 5, 4 byte values are added up, they give:

0x21DD09EC

You could simply do 0x21DD09EC / 5 but it's not a whole division. So instead you can just split 
it into 4 x 0x01010101 and 1 x 0x1dd905e8 = 0x21DD09EC

The Python shell is a good way to do this. - You can also use python to generate input:

./col "`python -c "print '\x01\x01\x01\x01' x 4 + '\xe8\x05\xd9\x1d' "`"

The hexadecimal characters are ordered backwards because of "little endianness".
Endianness refers to the ordering of bits within a binary representation of a number.

Little endianness orderind => reversed ordering of bits. Which is predominantly used for 
processor architecture x86/ARM + in this case as well.

