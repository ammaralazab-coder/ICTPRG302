# ROT3 Cipher Example
# This program encrypts and decrypts text by shifting each character
# three positions ahead (encryption) or backward (decryption)
# in a custom alphabet that includes letters, digits, and symbols.

# Define the custom alphabet
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()_-+={[}]\\|:;'\",<.>/?"

# --- ENCRYPTION FUNCTION ---
def encrypt(text, shift=3):
    """Encrypt text by shifting characters forward."""
    result = ""
    for c in text:
        if c in abc:
            index = (abc.find(c) + shift) % len(abc)
            result += abc[index]
        else:
            result += c  # keep unknown characters unchanged
    return result

# --- DECRYPTION FUNCTION ---
def decrypt(text, shift=3):
    """Decrypt text by shifting characters backward."""
    result = ""
    for c in text:
        if c in abc:
            index = (abc.find(c) - shift) % len(abc)
            result += abc[index]
        else:
            result += c
    return result

# --- Example Usage ---
cleartxt = "cat1"

# Encrypt
encrypted = encrypt(cleartxt)
print("Plaintext:", cleartxt)
print("Encrypted:", encrypted)

# Decrypt
decrypted = decrypt(encrypted)
print("Decrypted:", decrypted)
