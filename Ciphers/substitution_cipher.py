# Apply the substitution cipher, sending each char to another according to a map rule.
def apply_substitution_cipher(message, rule):
    # Make sure the message is a string.
    if not isinstance(message, str):
        raise ValueError("The message must be a string!")

    # Make sure the rule is injective so it can be reversed.
    danger = 0
    for item1 in rule.values():
            for item2 in rule.values():
                if item1 == item2:
                    danger +=1
    if danger > len(rule):
        raise Exception("The substitution rule must be injective!")

    # Encrypt the message by applying the rule to each character and concatenating them.
    encrypted_message = ""
    for ch in message:
        encrypted_message += chr(rule[ord(ch)])

    # Return the encrypted message.
    return encrypted_message

# Reverse the substitution cipher, inverting the cipher by applying the inverse map rule.
def reverse_substitution_cipher(ciphertext, rule):
    # Make sure the ciphertext is a string.
    if not isinstance(ciphertext, str):
        raise ValueError("The message must be a string!")

    # Apply the inverse rule to each character and concatenate them into the message.
    inv_rule = dict((c, p) for p, c in rule.items())
    message = ""
    for ch in ciphertext:
        message += chr(inv_rule[ord(ch)])

    # Return the message.
    return message



