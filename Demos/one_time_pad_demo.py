import sys; sys.path.append("../Ciphers")
from one_time_pad import *

# Convert a simple message to binary and display the result, along with the steps of the process.
message = "Hello there!"
print("Message:              " + message)
binary = convert_str_to_bin(message)
length = len(binary)
print("Binary:               " + binary + ", of length: " + str(length))
key = gen_key(length)
print("Key:                  " + key)
enc_msg = one_time_pad(binary, key)
print("Ciphertext binary:    " + enc_msg)
ciphertext_string = convert_bin_to_str(enc_msg)
print("Ciphertext:           " + ciphertext_string)
dec_msg = one_time_pad(enc_msg, key)
print("Decrypted binary:     " + str(dec_msg))
org_message = convert_bin_to_str(dec_msg)
print("Decrypted message:    " + str(org_message))
