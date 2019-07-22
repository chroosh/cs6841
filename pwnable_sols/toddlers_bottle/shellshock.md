# shellshock

Did some digging up and found that bash shocks were a series of security bugs found in 2014.

This program sets the values of the real, effective, setuser user and group id (resgid) to the 
value of his effective group id (egid) and then executes a vulnerable version of bash.

## Environment variables:
Are variables that are set outside of a program, typically through functionality built into the
operating system. Env variables usually exist in name value pairs.

## How does a Bash Shock work?
You can write functions in bash - and if you export them, bash stores the function definition
as an environment variable.

foo() { bar; }
>> environment var foo has the contents:
() { bar
}

My understanding of the vulnerability is that in early versions of bash, code that exists after
the end of the function definition is also executed. Example:

export foo='() { bar; }; echo "this will execute"'

Clearly, this isn't good because it allows you to very easily craft payloads from within a shell
to give yourself root access/do other malicious things.

New instances of the bash shell look for these environment variables and interpret them as
function definitions, which are evaluated + unintentionally executing the code after definition.

As a result, you can create an environment variable like this and add a /bin/cat flag to the end
to execute it.

export foo='() { echo 'hi'; }; /bin/cat flag;'
