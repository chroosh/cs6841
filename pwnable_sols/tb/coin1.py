import time
from pwn import *

# To speed up network response time we're going to run this script
# within pwnable server. This is also a good exercise to learn more 
# about computer networking.

def genList(lo, hi):
    l = []
    for i in range(lo, hi+1):
        l.append(str(i))

    return l


# So there'll be a lot of comments throughout this code to explain 
connection = remote('0', 9007)
connection.recv(10024)

# do this arbitrarily 100 times
for _ in range(100):
    # line is received from recv(1024) is going to be of form N=?? C=??
    line = connection.recv(1024).decode('UTF-8').strip().split(' ')
    n = int(line[0].split("=")[1])
    c = int(line[1].split("=")[1])

    #  print (n)   # N = number of coins
    #  print (c)   # C = number of chances
    

    lo = 0
    hi = n - 1
    for _ in range(0, c):
        mid = int((lo + hi)/2)
        print (lo, hi, mid)
        l = genList(mid, hi)
        message = " ".join(l)
        print ("message: " + message)
        connection.sendline(message)
        weight = int(connection.recv(1024).decode('UTF-8').strip())
        print ("weight: " + str(weight))
        # send l as a string to server
        if (weight % 10 != 0):
            lo = mid
        else:
            hi = mid
    print ("lo: " + str(lo))
    connection.sendline(str(lo))
    response = connection.recv(1024).decode('UTF-8')
    print (response)
    if (response == "Wrong coin!"):
        connection.sendline(str(hi))
    
print (connection.recv(1024).decode('UTF-8')
connection.close()





