# blackjack

"I like to give my flags to millionares"

Reading the source code given, in the betting() function, the 
amount of money the player is asked to bet is checked that it is
less than the amount of money they have.

If it's over, the game will ask the player again. But this number
is not checked. I noticed something was weird when the game asked
again for the bet it didn't include the $ sign.

This meant that the input validator wasn't a for loop and signaled
that it was more of a static once-off check.

millionares = 90 million should do the trick. Win the game and the
flag will appear up the top.
