Big write up 2/2

# fsb

Reading up on fsb seems that this challenge has something to do
with format strings and how they are vulnerable.

## format string attack
[Wiki] When the input string is evaluated as a command by the
application. Attackers can execute code, read stack, etc/

The attack can be executed when the application doesn't properly
validate the submitted input.

Supplying the %x in a printf function that is expecting more
arguments could allow you to read data off the stack.

Supplying a %n allows you to write an integer to locations in the process memory.

---

## Exploring the code in cat

I also noticed that there was use of "alloca". Upon reading the
man page, it stated that: "alloca" can be unsafe because it 
cannot ensure that the pointer returned, points to a valid/usable
block in memory. Might be something to note and can be exploited.

![](https://66.media.tumblr.com/aa99c5d218be6a31475f6e79dd586504/5fe76381c7391f65-6b/s540x810/0f71cf0f18367e06fc28e66d57b49b55198cac1d.png)

fsb() reads 4 format strings into the buffer (buf) of size 100 which is also printed out.

fsb() then reads a format string of length 100 and stores it in buf2, which is converted from a string into an unsigned long long.

If the converted long long is the same as the key that was read in main, execute a /bin/sh.
![](https://66.media.tumblr.com/ed2364e1c67b65486476ba3fce6a37ae/5fe76381c7391f65-f8/s540x810/660971f8a5f16928f014be736f8340223c6c62d9.png)

## objdump -D

Now thinking about it - both buf, buf2 and key are global variables, which are stored in the .bss / .data section, not the stack. This makes it a bit problematic because from all the exercises done so far, they were mostly centered around stack exploitation.

Unless there was a way to push them onto the stack? Let’s keep looking. We now know the addresses of key, buf and buf2.

`objdump -D fsb`

(objdump -D disassembles everything, including non executable sections like .bss)

![](https://66.media.tumblr.com/216c9b99a7e3ad342eac3a2b4705f9df/5fe76381c7391f65-f1/s540x810/ecb0448ddec0da214792e3d8c7d94408ca6242ca.png)

## Exploring code in gdb (looking for what happens to buf)

If we look at the disassembly, we can see that 0x804a100 (buf) is moved onto the stack position $esp+0x4. After the read call, the contents of buf are moved into $eax in order to be printed out.

Now let’s have a look at the stack. Gives me an idea - you can push global vars onto the stack so maybe we can do something similar with key?

![](https://66.media.tumblr.com/3d6ced5e19e19d3db6f029303a65d9ea/5fe76381c7391f65-b5/s540x810/a0933a56090cc28a6fb644fa2ac6c7cd0bfc421a.png)

## Exploring the stack in gdb
Doing [x/50wx $esp] prints out 50 words in hexadecimal from the stack pointer onwards. This is also known as a stack dump - essentially dumping all the contents of the stack for you to see.

![](https://66.media.tumblr.com/e43dbad7f2467e199743f32606c88a7b/5fe76381c7391f65-b0/s540x810/32a1467bcf2b667f926523b5c57009a27ebf3d62.png)

Each row represents a 0x10 increase in memory address, equal to 16 bytes each row. That means each memory address in the stack is 4 bytes. Makes sense because a word is 16 bytes.

You can view this diagram as an interpretation of the stack growing “down”.

We also notice that there are two values on the stack that point to another value on the stack. (self referential) That means if we can write the address of one variable to a stack, we can probably set the value they point to.

- 0xffba8180 is argument 14. It points to argument 20
- 0xffba8184 is argument 15. It points to argument 21

## Solution

Good points from another solution:
- A self referential stack means that %n can write data without 
leaking locality information
- Two refs that point to other values on the stack allows us to
control two values at once.

A recap - the addresses of things that are important to us are:
08040a60: key
08040a80: buf2
08040a80: buf

### Format string 1
Using %134520928c (which is 0x08040a60 in decimal) to output exactly 0x08040a60 bytes. Add %14$n to the string to write this value: address of (key) to the 14th argument. (Position 14 on the stack dump)

You also want to write to the 15th argument, which is 4 bytes greater. So you add 1111 (symbolising 4 bytes) to 0x08040a60 to get 0x0804a064 and store that in the 15th argument, %15$n.

> %134520928c%14$n1111%15$n

### Format string 2
You want to write 0x00000000 to the memory pointed to by args 20
and 21. (ie - what args 14 and 15 are pointing to) 

Essentially now the address of the key is now stored on the stack
in args 14 and 15. Args 14 and 15 point to args 20 and 21. So if
you set args 20 and 21 to 0x00000000, the key is now 0x00000000

> %20$n%21$n

Format strings 3 and 4 are whatever you choose.

All you need to do now is pass 0 into buf2, and it will pass the auth and launch a shell (/bin/sh)

![](https://66.media.tumblr.com/5115e102356750c52883c062dd5949a9/5fe76381c7391f65-23/s540x810/6c022641d872d0e26d39085524c5c6c7c448debe.png)

## extras

- Make sure to output into /dev/null and then redirect the output
to stdout

- (>&2 cat flag) - I’m not entirely sure what this does. I know >&2 
outputs to stderr the "cat flag" and that works because it's in
a shell. But idk why it's in brackets or so.
