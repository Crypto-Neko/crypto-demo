import random as rand

# Apply the affine cipher to a message (string)
def apply_affine_cipher(message, k):
    # Make sure the message is a string and the key is (a, b) with a,b in Z_128 and (a, 128) = 1
    if not isinstance(message, str):
        raise ValueError("The message must be a string!")
    if not isinstance(k, tuple):
        raise ValueError("Key should be a tuple (a, b) with a,b in Z_128 and (a, 128) = 1.")
    if not is_coprime(k[0], 128) or not k[1] in range(0, 128):
        raise ValueError("Key should be a tuoke (a, b) with a,b in Z_128 and (a, 128) = 1.")

    # Send the ASCII value x of each character in the message to ax + b
    encrypted_chars = []
    for ch in message:
        encrypted_chars.append((ord(ch)*k[0] + k[1]) % 128)

    # Convert the encrypted ASCII values back into characters and compose them into a string.
    encrypted_message = ""
    for ch in encrypted_chars:
        encrypted_message += chr(ch)

    # Return the encrypted message.
    return encrypted_message

def reverse_affine_cipher(ciphertext, k):
    # Make sure the message is a string and the key is (a, b) with a,b in Z_128 and (a, 128) = 1
    if not isinstance(ciphertext, str):
        raise ValueError("The message must be a string!")
    if not isinstance(k, tuple):
        raise ValueError("Key should be a tuple (a, b) with a,b in Z_128 and (a, 128) = 1.")
    if not is_coprime(k[0], 128) or not k[1] in range(0, 128):
        raise ValueError("Key should be a tuoke (a, b) with a,b in Z_128 and (a, 128) = 1.")

    # Apply the inverse: y |--> a^{-1}(y -b b)
    chars = []
    for ch in ciphertext:
        chars.append((get_inverse(k[0], 128)*(ord(ch) - k[1])) % 128)

    # Decrypt the ASCII characters and compose them into the message.
    message = ""
    for ch in chars:
        message += chr(ch)

    # Return the decrypted message.
    return message

# Check if a and b are coprime; used to ensure the validity of the key.
def is_coprime(a, b):
    # Search for a common divisor.
    q = int((min(a, b))**(1/2))
    for i in range(2, q+1):
        if int(a/i) - a/i == 0 and int(b/i) - b/i == 0:
            return False
    
    # Return True if no common divisor was found.
    return True

# Compute the inverse of the integer a mod n.
def get_inverse(a, n):
    # Check that an inverse exists.
    if not is_coprime(a, n):
        return("The integers must be coprime!")
    
    # Search for an inverse and return it.
    for i in range(2, n):
        if (a*i) % 128 == 1:
            return i


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
