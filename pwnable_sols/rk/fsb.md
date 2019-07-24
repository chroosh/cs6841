# fsb

Reading up on fsb seems that this challenge has something to do
with format strings and how they are vulnerable.

## format string attack
[Wiki] When the input string is evaluated as a command by the
application. Attackers can execute code, read stack, etc/

The attack can be executed when the application doesn't properly
validate the submitted input.

<!-- this should rewritten with consideration to what caff said -->
Supplying the %x in a printf function that is expecting more
arguments could allow you to read data from the stack.

---

## Exploring the code in cat
I also noticed that there was use of "alloca". Upon reading the
man page, it stated that: "alloca" can be unsafe because it 
cannot ensure that the pointer returned, points to a valid/usable
block in memory.

Might be something to note and can be exploited.

fsb() reads 4 format strings into the buffer (buf) of size 100
which is also printed out.

fsb() then reads a format string of length 100 and stores it in
buf2, which is converted from a string into an unsigned long long.

If the converted long long is the same as the key that was read 
in main, execute a /bin/sh

<!-- Okay looking at a solution now. -->

## Exploring code in gdb (looking for where buf is)
Exploring the code in gdb. We want to find what the address of 
buf is. If we look at the fsb.c file, we can see that the 
printf(buf) is being called after the read.

If we look at the disassembly, we can see that [0x804a100] is 
moved into $eax before the printf call. Using pwndbg it will show 
us that it contains the buf. (%x.%x.%x ... %x.%x.x)

caff: %x%x%x%x%x will just print the next five elements off the
stack

## Exploring the stack in gdb
Doing [x/50wx $esp] should print out 50 words in hexadecimal from
the stack pointer onwards.

adamt: each word is 4 bytes so each line is 16 bytes.

Effectively, this prints out the stack (a stack dump). The addr's
increase as you go down, so this demonstrates the stack growing 
(down)

If we type in something ["hello"] and run the x/50wx $esp, you can
see that the nothing that we entered via stdin is actually being 
written to the stack.

> The first letter is a "h" which has a hex value of \x68. There is 
no 68 on the stack (as shown)

We also notice that there are two values on the stack: (refs)
- 0xffea19c0
- 0xffea19c4

Which point to another value on the stack. This means we can probs
use these to write to the stack to get our flag. (Self-referential)

## Solution
So lets us pwntools to do just that // or just no pwntools

From another solution:
- A self referential stack means that %n can write data without 
leaking locality information
- Two refs that point to other values on the stack allows us to
control two values at once.
- The refs and the targets exist above the randomised stack chunk
meaning that the positions and the positions they reference are
static.

The addresses of things that are important to us are:
08040a60: key
08040a80: buf2
08040a80: buf

// This is probably an easier way to tell where buf is located.

### Format string 1
Using %134520928c (which is 08040a60 in hex) to output exactly
08040a60 bytes. Add %14$n to the string to write this value:
address of (key) to the 14th argument. (Position 14 on the stack
dump)

You also want to write to the 15th argument, which is 4 bytes
greater. So you add 1111 (symbolising 4 bytes) to 08040a60 to get
0804a064 and store that in the 15th argument, %15$n.

> %134520928c%14$n1111%15$n

### Format string 2
You want to write 0x00000000 to the memory pointed to by args 20
and 21. (ie - what args 14 and 15 are pointing to) 

Essentially now the address of the key is now stored on the stack
in args 14 and 15. Args 14 and 15 point to args 20 and 21. So if
you set args 20 and 21 to 0x00000000, the key is now 0x00000000

> %20$n%21$n

fs 3 and 4 are whatver you choose.

All you need to do now is pass 00000000 in buf2, and it will pass 
the auth and launch a shell (/bin/sh)

* Make sure to output into /dev/null and then redirect the output
to stdout

(>&2 cat flag) << I dont really know what this does. I know >&2 
outputs to stderr the "cat flag" and that works because it's in
a shell. But idk why it's in brackets or so.

