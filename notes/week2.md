# Week 2

## Security by Design
Spend resources to factor in security in the initial design of the system instead of
having it factored in as an afterthought or retrofit.

Build something such that if one part breaks the entire system isn't compromised.
Compartmentalisation is great here.

Examples: Apollo 11/13, submarines

## Living in complexity
The ant colony itself is a creature - drawing an analogy to human anatomy, our cells
don't make decisions for us, instead it's a collective / emergent property of our selfs

In ant colonies, they all have rigid roles. But ants don't have high IQ's. The reason
why the ant colonies have thrived is because of their inability to disconform to the
rules and structure that has been set.

Now as humans we have free will, and can break out and not follow rules. The complexity
of the human race is borne from our ability to interact with each other by choice.

(Something to think about) Who in the ant colony came up with the ideas? There must be
someone right? Or is this an example of a human applying human social paradigms to a
species that isn't human?

## Physical Security
That's actually a good point - although we deal with everything in a virtual world, 
if access to something is granted in the physical world, none of it really matters?

Richard gave a fantastic example of side channels - you could always tell when big
banks were working on big deals by looking at their windows at night. As the deal gets
closer and closer more people's lights are on and you see people walking in and out
during weird times. Wouldn't be especially hard to do some social engineering and then
find out who the deal actually involves - and then you would have insider information.

Now all of this information is closed within the building - but the idea is that traces
are left out in the open world. And this is what it means by "every contact leaves a
trace in the physical world"

So always consider physical security measures before software security measures.

## Vignere Cipher
Essentially a Caesar cipher in that the letters are shifted along the alphabet but
instead of shifting the entire text by X, we shift the letters by a predetermined
numerical "password" that loops around.

ABBA = 0, 1, 1, 0
HELLO ==> HFMLO
(+0, +1, +1, +0)

### Kasiski Test
Used to defeat cuphers where password/offset repeats (Vignere) 

Find the length of the key by looking for repetitions, and then line up each section
and solve the lined up letters as a single substitution cipher.

<!--TODO-->
### Index of Coincidence
Indicator used in cryptanalysis to evaluate the global distribution of letters in an
encrypted message for a given alphabet. If the index is high, the message is similar
to plain text (and has probably been encrypted by transposition/monoalphabetic sub)

Transposition sub = letters in a message are moved around. IE - reversed.

If the index is low, then the message is similar to random text and has been encrypted
using a polyalphabetic cipher (letter replaced by multiple other ones)

Formula on notes.

<!--TODO-->
## Enigma Machine
Electromechanical rotor mechanism that scrambles the 26 letters of the alphabet using
a substitution + almost infinite password.

Weaknesses:
- Repeatedly used stereotypical expressions
- Repetition of message key
- Easily guessed keys
- Re-transmitting a message on different cipher networks
- Not allowing repetitions

<!-- TODO -->
## One Time Pad
OTP is an encryption technique that cannot be cracked, but requires the use of a one
time, pre-shared key the same size as or longer than the message being sent. In this
technique, a plain text is paired with a random secret key (the OTP). Then, each bit 
or character of the plaintext is encrypted by combining it with the corresponding bit
or character from the pad using modular addition.

Like Vignere, but the password is the length of the message and completely random.
Once used, the cipher should be discarded.

# Type 1 vs Type 2 Errors
Type 1: False positive - medical test saying you have a disease when you dont.
Type 2: False negative - medical test saying you don't have a dease when you do.


# Tutorial Case Study - Houdini
Harry Houdini was a stage magician who loved publicly exposing mediums (people who 
claim to possess the ability to speak to dead people) as fakes and frauds. Before
passing away, he agreed with his wife such that if by some way he was able to 
communicate after death, he would use the message "Rosabelle believe"

1. State and briefly justify the most important properties your protocol should have
- Message should be longer / contain more random words - increases entropy.
- Easily remembered by Houdini and his wife - inside jokes?
- Shouldn't be easily traced to Houdini or his wife - inside jokes?
- Maybe stay away from English words, or words altogether. Actions?

2. Give your protocol
- Houdini and his wife agree on a 5 word phrase and an action into a message
- This message is encrypted using a public key and published into newspaper
- Medium who claims Houdini is communicating through them must decrypt the message
using Houdini's private key and perform the action while delivering the 5 word phrase.

- I liked the idea of saying "prove to me so that she doesn't reveal the format of the
protocol even if the medium somehow decodes the 5 word phrase
