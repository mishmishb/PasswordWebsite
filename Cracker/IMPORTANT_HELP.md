# Search

Sort all returned entries by token length

Pop first entry - compare to stored input and remove entry (as well as any with i and j values the intersect first entry) from input
  * input: t3sting
  * entry: t3st
  * output: ing
--> output becomes new input and repeat
  * keep i and j values?
**Run whatever is leftover through bruteforce entropy calculator**
Based on the dictionary each part comes from, run through relevant entropy calculator

**Break ties using rank? would need to reverse this part somehow**

# Guesses

How to calculate entropy of words in a dictionary?
Get individual entropies and add them up

Dictionary guesses:
	log2(rank) + uppercasing entropy + l33t entropy

to calculate entropy of words with an uppercase
rank +

# Uppercases

Remember position of uppercase letter, if consistent then don't increase guesses as much?

# L33T

Currently goes through each letter in table and checks if the current sub is in the password

better than going through password and fetching potential subs?
  
## Changes from zxcvbn (excl. search)

Show how the model has to assume the password's structure
Show how long the crack would take if this assumption was taken away? - How to account for bruteforce?

Ability to account for one or two characters being inaccurate?
