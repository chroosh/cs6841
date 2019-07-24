# mistake

A mistake can be seen immediately in the first comparison where there is no priority given 
between the fd = open assignment and the fd < 0 comparison.

## exploring the sauce

Without the brackets assigning the return value from open to the fd, the return value from open()
is first compared to less than 0. Since the return value is an integer larger than 2 for a file
descriptor. This evaluates to 0 which is assigned to the fd variable. Hence fd will be routed to 
stdin.

This plays nicely in the next chunk of code where once again the return value of the read function
will be compared to > 0 and then the evaluated value assigned to len.

Read is reading from stdin, into pwbuf and of size pwlen (10). The amount of successful bytes
read is returned. So if you send a full 10 bytes into stdin, len will get assigned a value of 10.

After, a new pwbuf2 is created of siz pwlen+1 (11) The scanf takes in 10 characters in the string
and assigns it to pwbuf2. The last byte of the pwbuf2 is not written.

pwbuf2 is then XOR'ed against an XORKEY of 1. It's worth noting that only the first 10 bytes get
XOR'ed. The last byte does not.

## payload

If pwbuf and pwbuf2 are compared to a true - it should cat a flag.

So essentially, find two characters such that XOR'ing one character will result in another 
character. 1 and 0 work well - 60 ^ 1 = 61 and 61 ^ 1 = 60.

When running the program, runtime wil automatically expect something from stdin because of the
operator mis-grouping at the top of the main() function. Enter 10*1 and then 10*0 to retreive flag.


