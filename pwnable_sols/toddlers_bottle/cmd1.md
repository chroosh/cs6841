# cmd1

Two functions filter and main

* Main:
Putenv adds the env variable /thankyouverymuch to the environment list - essentially changes
where the system looks for, for the folder containing executables (cat - etc) (usually /bin
instead of /thankyouverymuch)

* Filter
Will return a value to invoke an early exit for the main function if the argv[1] conains any
instance of the strings "flag" "sh" or "tmp".
To get around this we can echo each letter individually - "f""l""a""g"

We know that the flag is in the home directory so now we need to find a way to cat it so that
we can know what's inside.

The system doesn't know what "cat" is specifically because the path has now changed to 
/thankyouverymuch as opposed to bin. We can use "which cat" to find that cat is stored at
/bin/cat

So we can do ./cmd1 "/bin/cat \"f\"\"l\"\"a\"\"g\"" - making sure to escape the quotes.
