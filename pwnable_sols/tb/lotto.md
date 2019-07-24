# lotto

Looking at the code, the play function reads a file to import
the lotto numbers into a lotto buffer.

Lotto buffer is made up of char's - ie ASCII chars. The comment
also indicates that lotto cannot go above 45.
 
lotto[i] = (lotto[i] % 45) + 1

If we look at an ascii table, the first 32 entries are all...
not numbers or letters. It's filled with things like carriage
return, backspace, etc.

These represent non-printable control characters and cannot be
typed in. So the only characters you can use are: 

- !
- "
- #
- $
- %
- &
- '
- (
- )
- *
- +
- ,
- -

## payload

Looking at the for loop, another bug becomes apparent. The 
double for loop will iterate for all of the characters in the
submit buffer for one character at a time in the lotto buffer.

That means that if you have even one character that matches,
the match count will increment to 6. Usually, the match variable
should be reset on each iteration of the first for loop. And
the for loops should be replaced with a single for loop that 
iterates an index that access both lotto and submit at the same
index.

Trying !!!!!! a couple times should give you the flag.
