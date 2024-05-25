import random as rand
import sys; sys.path.append("../Ciphers")
#from shift_cipher import *
from vigenere_cipher import *

# A basic test with a 4-tuple.
message = ["Hello", " there!", "How are", "you?"]
k = (3, 17, 98, 73)
ciphertext = apply_vigenere_cipher(message, k)
print(ciphertext)
print(reverse_vigenere_cipher(ciphertext, k))

# A randomized example.
message = ["this", "is", "a", "really", "good", "test"]
n = rand.randint(1, 6)
message = message[:n]
k = ()
for i in range(0, n):
    k += (rand.randint(0, 127),)
ciphertext = apply_vigenere_cipher(message, k)
print(ciphertext)
print(reverse_vigenere_cipher(ciphertext, k))
