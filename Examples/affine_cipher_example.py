import random as rand
import sys; sys.path.append("../Ciphers")
from affine_cipher import *

#### EXAMPLE CODE ####
message = "This is a message!!"
a = rand.randint(0, 127)
while is_coprime(a, 128) == False:
    a = rand.randint(0, 127)
b = rand.randint(0, 127)
k = (a, b)
ciphertext = apply_affine_cipher(message, (a, b))
print(ciphertext)
print(reverse_affine_cipher(ciphertext, k))
