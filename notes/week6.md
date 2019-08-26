# Tutorial

If you are Mike Burgess, what recommendations would you have for the Australian Prime 
Minister to produce 10 recommendations for actions to be taken regarding the main 
threats we face in the cyber domain of war.

1. Updating legacy infrastructure (especially infrastructure involved in essential functioning 
of society - utilities, etc) to modern equivalents.
2. Build creative and isolated redundancy systems for communication and navigation systems. 
Provides redundancy without dependencies.
3. Educate the security industry on current exploits - buying exploits from people.
4. Setting up an official public channels that verifies news to the public. Removes mis-
information and fake news.
5. More comprehensive background checks for employees dealing with secure employees. Lowers the 
chance of whistleblowers.
6. Strengthen politcal and diplomatic ties with other countries to prevent potential attacks.
7. Securing critical research and intelligence facilities. (?)
8. Investing in security education at secondary + tertiary levels. Allows the gov draw talent 
from internally instead of overseas.

# Module 6

## One-time pad
[Wiki excerpt]
Encryption technique that cannot be cracked, but requires the use of a one-time pre-shared key,
which is the same size as, or longer than the message being sent.

In this technique, the plaintext is paired with a random secret key. Each bit or character of
plaintext is encrypted by combining it with the corresponding bit or character from the pad
using modular addition.

If the key is:
1. Truly random
2. At least as long as the plaintext
3. Never reused in whole or in part
4. Kept completely secret

Then the resulting ciphertext will be impossible to decrypt or break.

One time (one only looks at police one time) early implementations had keys that were
distributed as a pad of paper, so that the top sheet could be torn off and destroyed after use.

https://99percentinvisible.org/episode/vox-ex-machina/

This is an pseudoapplication of a one time pad that was built in order to safety transmit
messages during WW2. SIGSALY operated by having a number of terminals located where messages
were transmitted via shortwave radio. Each terminal also had a top secret pair of vinyl
photograph records containing an identical but random noise which acted as the single use (one)
keys to the encryption and decryption process.

To decrypt a OTP using the XOR method
1. Guess a word that might appear in one of the messages
2. Encode the word from step 1 to a hex string
3. XOR the two cipher-text messages given
4. XOR the hex string from step 2 (guessed word) at each position of the string from step 3
5. When step 4 results in readable text, we can guess the english word and expand search

## Thread Modelling
This feels an awful like consulting.
Building a threat treee // really similar to building an issue tree to analyse 

DREAD:
Damage, Reproduceability, Exploitability, Affected users, Discoverability

STRIDE: (Security threats in 6 categories)
Spoofing (of user identity)
Tampering (internal modification of products)
Repudiation (rejection of a proposal or idea)
Information disclosure (privacy breach or data leak)
Denial of service (DoS)
Elevation of privilege (rootkit)


## 5G Networks
