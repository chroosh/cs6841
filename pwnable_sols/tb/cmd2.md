# cmd2

(Yes I did look up the solution to this one)

Building on from cmd1. Running ./cmd2 cat - still says cat not found, which means we need to
do similarly /bin/cat. But you cant now because the filter now checks for "/"

To get around this there is an option to execute a builtin called "command" with an option -p
to supply a default value of path.

So far, our command looks something like this:
./cmd2 "command -p cat lol"

We can then re-use the technique in cmd1 to use escaped quoted individual letters in place of
"flag"

./cmd2 "command -p cat \"f\"\"l\"\"a\"\"g\""
