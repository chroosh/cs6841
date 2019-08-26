# Week 5

I gave up on writing stuff down and I figured my fingers need to do some work instead of my 
wrist so here we go.

# Module 5

## Cryptographic properties
Preimage Resistance - given the hash it should be hard to find the original message.

H(???) = pzz
// Can you think of a word when hashed, results in "pzz"?

Second Preimage Resistance - given the hash and the original message, it should be hard to come
up with a second message that has the same hash.

H(icehouse) = chs
H(???) = chs

// It should be hard to figure out another word that also has has the hash "chs"
// Can you think of another word that when hashed using the NSHA-1 algorithm results in "chs"?
// That's how you break the second preimage resistance.

Collision Resistance - It should be hard to choose any two messages that result in the same hash

Hash(message1) != Hash(message2)

// I think the difference between this and Second Preimage Resistance is that the former is 
// broken when you know one and find one, whereas collision is where you know none and find
// both.

## Passwords

Rules for choosing a strong password:
- Longer the better
- Unique for each use
- Capital letters, numbers, symbols and lowercase
- Avoid words from dictionary

You can try to calculate how long it would take to bruteforce a password. OR you can use a
password manager.


All the passwords in a password manager are usually encrupted using AES-256 bit encryption using
a single master password.

Methods for coming up with a password:
- Passphrase + incorporate numbers and symbols
- Abbreviate a passphrase by choosing the first letter
- xkcd, using a mental picture made up of 4-5 words.



