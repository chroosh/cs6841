# fd

Using cat.fd displays the contents of fd.c out to standard output. 
The focus of this challenge is surrounding the understanding of file descriptors

0 - STDIN
1 - STDOUT
2 - STDERR

The code subtracts 0x1234 from argv[1], and treats that as a file descriptor.
So if you input 4660 (equivalent to 0x1234) in hex, the code will open an fd
of value 0, allowing you to write to STDIN.

Typing "LETMEWIN" as shown from inside the fd.c will retrive flag.

