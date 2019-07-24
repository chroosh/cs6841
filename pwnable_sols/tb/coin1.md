# coin1

use a binary search to identify which coins weigh less and are fake

for this challenge i will endeavour to use pwntools to communicate 
with servers easier, and implement the binary search in python.

i knew the solution involves implementing a binary search to test 
the weights of the coins.

we open a remote connection to '0' - since we'll be using pwnable's
own server to eliminate network latency.

have a for loop up to 100. we want to find the counterfeit coin 100
times. so we'll be running the binary searching code 100 times.

## networking using pwnable
connection = remote('0', 9007)  	# connects me into nc server
connection.recv(1024) 						# receives 1024 bytes from con
connection.sendline(message) 			# sends something to connection

from there it was a matter of implementing a binary search correctly
using python and making sure the lines were sent correctly.

i used a helper function to generate the string of numbers that were
sent to the connection to be weighed.

for receiving connections, you need to decode them until utf8

connection.recv(1024).decode('utf-8')

and depending on some instances you will also need to .strip() to 
remove whitespace.

