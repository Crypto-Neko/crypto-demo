import random as rand

# Apply the shift cipher to a message (string).
def apply_shift_cipher(message, k):
    # Shift the ASCII value of each character in message by k and store them in an array.
    encrypted_chars = []
    for ch in message:
        encrypted_chars.append((ord(ch) + k) % 128)
    
    # Convert the encrypted ASCII values back into characters and compose them into a string.
    encrypted_message = ""
    for ch in encrypted_chars:
        encrypted_message += chr(ch)

    # Return the encrypted message.
    return encrypted_message

# Reverse the shift cipher by applying its inverse to the ciphertext (string).
def reverse_shift_cipher(ciphertext, k):
    # Shift the ASCII value of each cahracter back by -k and store them in an array.
    chars = []
    for ch in ciphertext:
        chars.append((ord(ch) - k) % 128)

    # Convery the decrypted ASCII values back into characters and compose them into a string.
    message = ""
    for ch in chars:
        message += chr(ch)

    # Return the decrypted message.
    return message


#### EXAMPLE CODE ####
message = "Message received."
k = rand.randint(0, 127)
ciphertext = apply_shift_cipher(message, k)
print(ciphertext)
print(reverse_shift_cipher(ciphertext, k))
