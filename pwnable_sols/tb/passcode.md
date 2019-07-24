# passcode

Examination of the shows three sections: main, welcome and login. I'm pretty sure most of the
action is all in the login() function.

When running the binary, the code segfaults when the input is an integer but not when it is a
standard ascii character IE - 'h'

I tried using GDB to pinpoint exactly which line was causing the segfault.

Started looking online after this.

Something noticed was that neither of the scanf's write the input to &. IE the variables of
passcode1 and passcode2 aren't dereferenced.

Disassembling welcome and login shows:
lea edx [ebp-0x70] // we now know that the variable (Name) is ebp-0x70
lea edx DWORD PTR [ebp-0x10] // we know that the variable (passcode1) is ebp-0x10
lea edx DWORD PTR [ebp-0xc]  // we know that the variable (passcode2) is ebp-0x20

The difference between the name and passcode1 variable is 96, which is smaller than the size of
the name buffer (100). As a result, the last 4 bytes are read into password1?

## Payload
If we fill the name buffer (with 96 * 'A') and pass the address of fflush into the last 4 digits
into password1.

fflush is used to clear the stream/buffer being written to. (I think it's the name buffer)

We will then be able to use the first scanf() to overwrite the fflush() function with system() 
and retrieve the flag.

We can find the addresses of fflush() and system() using 
objdump -R passcode

Final payload looks like:
python -c "print('A' * 96 + '\x04\xa0\x04\x08' + '134514147')" | ./passcode

## Global Offset Table
The Global Offset Table is a place in which binary stores the address of functions that are
unknown at compile time but is updated at runtime by a dynamic linker. Once a program has been
run once, the addresses of functions can be directly retrieved from the GOT, instead of re-using
the dynamic linker.


