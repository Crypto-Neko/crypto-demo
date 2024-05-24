from shift_cipher import *

# Apply the Vigenere cipher: apply the shift cipher once to each element of the message tuple.
def apply_vigenere_cipher(message, k):
    # Validate input.
    if (not isinstance(message, tuple) and not isinstance(message, list)) or (not isinstance(k, tuple) and not isinstance(k, list)):
        return("Message and key must be n-tuples.")
    if not len(message) == len(k):
        return("Message and key must be of the same size.")
    for m in message:
        if not isinstance(m, str):
            return("Every element of the message tuple must be a string.")
    for ki in k:
        if not isinstance(ki, int) and ki in range(0, 127):
            return("Every element of the key tuple must be an integer in Z_128.")

    # Encrypt the message by applying the shift cipher to each element of the message tuple.
    n = len(k)
    encrypted_message = message.copy()
    for i in range(0, n):
        encrypted_message[i] = apply_shift_cipher(message[i], k[i])

    # Return the encrypted message tuple.
    return(encrypted_message)

# Rever the Vigenere cipher, reversing the shift cipher on every element of the ciphertext tuple.
def reverse_vigenere_cipher(ciphertext, k):
    # Validate input.
    if (not isinstance(ciphertext, tuple) and not isinstance(ciphertext, list)) or (not isinstance(k, tuple) and not isinstance(k, list)):
        return("Message and key must be n-tuples.")
    if not len(ciphertext) == len(k):
        return("Message and key must be of the same size.")
    for c in ciphertext:
        if not isinstance(c, str):
            return("Every element of the message tuple must be a string.")
    for ki in k:
        if not isinstance(ki, int) and ki in range(0, 127):
            return("Every element of the key tuple must be an integer in Z_128.")
    
    # Reverse the encryption by reversing the shift cipher on each element.
    n = len(k)
    message = ciphertext.copy()
    for i in range(0, n):
        message[i] = reverse_shift_cipher(ciphertext[i], k[i])

    # Return the decrypted message.
    return(message)
