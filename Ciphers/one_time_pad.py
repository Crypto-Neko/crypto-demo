import random as rand

# Convert a message (string) to a binary string and give the length in digits.
def convert_str_to_bin(message):
    # Check for invalid input.
    if not isinstance(message, str):
        return("Message must be a string.")

    # Conver the message to binary.
    binary = ""
    for ch in message:
        binary += format(ord(ch), '08b')

    # Return the binary string.
    return binary

# Convert a binary string back to a message.
def convert_bin_to_str(binary):
    # Check for invalid input.
    if len(binary) % 8 != 0:
        return("Enter a binary representation of an ASCII string.")
    
    # Build the message from characters in the binary array.
    message = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message += chr(int(byte, 2))

    # Return the message.
    return message

# Generate a key for OTP.
def gen_key(length):
    # Generate the key randomly.
    key = ""
    for i in range (0, length):
        key += str(rand.randint(0, 1))

    # Return the random key.
    return(key)

# Apply the one-time-pad given a binary string and a key. Also serves as the inverse!
def one_time_pad(binary, key):
    # Check for invalid input.
    if len(binary) != len(key):
        return("Binary string and key must be of the same length.")
    
    # Apply OTP to encrypt or decrypt the message.
    result_bin = ""
    for i in range(0, len(binary)):
        result_bin += str((int(binary[i]) + int(key[i])) % 2)

    # Return the result of OTP.
    return result_bin
