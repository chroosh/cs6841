# memcpy

In essence, the numbers inputted must have 16 bit alignment.
8
16
32
72
136
268
600
1208
2408
4808

You can if you want, add in a line into the source code which
prints out the destination after the line:

dest = malloc( size );

printf ("dest : %p\n", dest)

This way, you need to ensure that the destination address is 
always divisible by 16.

