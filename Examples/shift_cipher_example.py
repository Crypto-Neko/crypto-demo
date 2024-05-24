import random as rand
import sys; sys.path.append("../Ciphers")
from shift_cipher import *

message = "Message received."
k = rand.randint(0, 127)
ciphertext = apply_shift_cipher(message, k)
print(ciphertext)
print(reverse_shift_cipher(ciphertext, k))
