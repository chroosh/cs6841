# input

- argv (command line arguments)
stage 1 argument count must be equal to 100
arg at position 'A' must be equal to \x00 or ""
arg at position 'B' must be equal to \x20\x0a\x0d

You can use python to create a list of args and pass them via
execv()

- stdio 
Reading from file descriptor 0 and 2 which is stdin and stderr 
respectively. So in theory you should be able to pipe these in.

In python you can use os.pipe() to create pipes - check input.py
Use os.write to write the piped values to stdinw and stderrw

- env
Create an environment variable "deadbeef" to the value "cafebabe"
You can use os.putenv.

- file
Attempts to open \x0a in read mode and attempts to read 4 bytes
in one object, from a stream pointed to by fd. It also attempts
to copy  \x00\x00\x00\x00 from the same fd.

Essentially, just create a file containing \x00\x00\x00\x00.

- networks
Sockets are essentially endpoints for sending and receiving data 
on a computer network...

Jokes this one I got a lot of help from. Should spend some time
one day and learn about networks properly.
