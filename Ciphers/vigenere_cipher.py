from shift_cipher import *

# Apply the Vigenere cipher, i.e. apply the shift cipher n times.
def apply_vigenere_cipher(message, k):

    n = len(k)
    encrypted_message = message.copy()
    for i in range(0, n):
        encrypted_message[i] = apply_shift_cipher(message[i], k[i])

    return(encrypted_message)

def reverse_vigenere_cipher(ciphertext, k):

    n = len(k)
    message = message.copy()
    for i in range(0, n):
        message[i] = reverse_shift_cipher(ciphertext[i], k[i])

