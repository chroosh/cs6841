# Week 7

## Tutorial
Stack vs Heap
Stack is used for data that are known at compile time whereas the heap is used for
for data that is generated at runtime.

Shellcode
Code that is used to pop a shell for you to run commands on.

## Misdirection
A form of deception in which the performer draws audience attention to one thing to distract it
from another.

Common examples of this include "wand waving" - or in a more practical security sense during a
CTF, sending someone a link pretending to be the flag, but instead directing them to malware.

## AES and Block Cipher Modes
[Openlearning excerpt]
DES (Data Encryption Standard) + AES (Advanced Encryption Standard) are examples of block
ciphers, which encrypt plain text a fixed amount of the file at a time. DES accepts 64 bits at a
time while AES accepts 128 bits.

The amount of bits accepted is known as the cipher block size. Because most files are larger
than 128 bits, we need to come up with a way to divide a file into 128 block sizes and encrypt
them all.

- ECB Electronic Code Book
Divide the file up into chunks of 128 bits and encrypt them separately. The main flaw of this
is that identical chunks will be encrypted to the same output, making analysis trivial.
That Tux penguin example was great.

- CBC Cipher Block Chaining
Incorporating the past block in each subsequent block. Each blogk is a result of all the blocks
before it. This is very good, Tux penguin is very happy. The problem with this is that Tux the
pengui will take quite a bit of time to encrypt because you cannot encrypt blocks in parallel.
The preceding block must be encrypted before the next one.

- CTR Counter Mode
Counter mode turns the AES block sipher into a pseudo-stream cipher. Recall stream ciphers work
by flipping each bit at a time. 

// A nonce is an arbitrary number that can be used just once in cryptographic communication
Instead of encrypting the plain text, CTR mode encrypts a random NONCE and counter value. For 
each subsequent block, the counter value is increased and the confusion/diffusion properties of
AES allow a small change in plaintext to result in a massive change to the cipher text.

This long strong of pseudorandom bits is treated like a stream cipher - the actual plaintext is
XORed with the output of the encryption of the NONCE and counter, and the real cipher is the
result of the XOR operation.

// Essentially, the nonce + counter undergoes block cipher encryption, and that is XOR'ed with
// the message in the plaintext to produce the cipher text.

This cipher doesn't suffer from the problems of ECB, but is parallisable. 
Funny thing when I did the exercise, Cipher 2 encoding an input 'a' will generate 96. The answer
is counter mode.

## Social Engineering
[Openlearning excerpt]
Social engineering via email still remains one of the most common ways for end users to be
compromised.

My strategy would involve sending some emails to do some recon and figure out who is repsonsible
for what in the company.

One way you can write a phishing message is by copying someone elses phishing message
