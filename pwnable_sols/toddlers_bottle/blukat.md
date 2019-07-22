# blukat

I started by looking at what was inside blukat.c

The first fgets takes input from a file called password and the
second fgets takes input from stdin. If you cat password it will
tell you that it's [permission denied]

1. You could run a brute force attack on stdin to try to match
the password.

2. Maybe "cat: password: permission denied" is the password that 
the binary is using.

If we copy paste it in when the binary asks for a password, we
get the flag :)

(And yes I did look up the solution)

I did some searching beforehand actually. A 12 character brute
force would take 2 centuries. So how long would a 100 character
brute force take?

1.90 million trillion trillion trillion trillion trillion trillion 
trillion trillion trillion trillion trillion trillion trillion 
trillion centuries

So you could just keep guessing things that might be obvious.
Things like:
- bluekat
- password
- prowl
- guess the password
- cat: password: permission denied
