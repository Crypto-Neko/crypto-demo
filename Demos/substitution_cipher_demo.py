import random as rand
import sys
sys.path.append("../Ciphers")
from substitution_cipher import *

# A basic rule that sends the nth ASCII character to the next ASCII character.
rule = {}
for x in range(128):
    rule[x] = (x+1) % 128
ciphertext = apply_substitution_cipher("Hi there!!1!", rule)
print(ciphertext)
print(reverse_substitution_cipher(ciphertext, rule))

# A "bad rule" that sends every character to a--this is NOT injective and will fail!
bad_rule = {}
for x in range(128):
    bad_rule[x] = 97
apply_substitution_cipher("This will not work.", bad_rule)
