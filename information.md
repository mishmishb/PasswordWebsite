check word lists first
spatial keyboard patterns too (QWERTY, maybe DVORAK and numeric keypad)
repeats (aaaaa)
sequences (12345, abcdefgh)
years (1900-2019)
dates (28-12-1995, 281295)
uppercasing
l33t subs

use substring of input, when a word is matched remove from the string and check remaining string for more words
if nothing is found from remaining characters, consider first character 'random' and check remaining characters - e.g:
    lemontdrop -> 'lemon', 'tdrop' -> 'lemon', 't', 'drop'  OR 
    lemontxgdrop -> 'lemon', 'tdrop' -> 'lemon', 't', 'xgdrop' -> 'lemon', 'tx', 'gdrop' -> 'lemon', 'txg', 'drop'
    
for 'random' strings, check against criteria at top of this file before concluding they are 'random' if no matches are made

Once each pattern is isolated, ('Mich43lxcv2019' -> Dict: 'Mich43l', Spatial: 'xcv', Date: '2019') calculate entropy for each individual pattern

**It is important** that when checking patterns, overlapping matches are taken care of. The lowest entropy option should end up selected

**ZCXCVBN EXAMPLE**

zxcvbn calculates a password’s entropy to be the sum of its constituent patterns. Any gaps between matched patterns are treated as brute-force “patterns” that also contribute to the total entropy. For example:
```
entropy("stockwell4$eR123698745") == surname_entropy("stockwell") +
                                     bruteforce_entropy("4$eR") +
                                     keypad_entropy("123698745")
```

The problem with this method is it assumes the attacker already knows the structure of the password, e.g. *surname-bruteforce-keypad*

A normal cracking tool would start with simpler structures, going through each until eventually reaching the actual structure, for example:

*correcthorsebatterystaple* is *word-word-word-word*

A cracking tool might start *word* then *word-word* before reaching *word-word-word-word* - Also other structures too

**looking into entropy of going through all possibilities of different structures would set my tool apart from ZXCVBN**

**ZXCVBN assumes the attacker already knows the structure as it is safer to underestimate**

**I would need to find what structures people choose most somehow**

Read end of: https://blogs.dropbox.com/tech/2012/04/zxcvbn-realistic-password-strength-estimation/

for ideas
