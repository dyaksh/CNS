def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
        
    for char in text:
        # Shift all ASCII characters
        new_char = chr((ord(char) + shift) % 256)  # Using 256 to cover all possible ASCII values
        result += new_char
        
    return result

# Get user input
inp = input("Enter something here: ")
shift = int(input("Enter the shift: "))

# Encrypt
encrypted_message = caesar_cipher(inp, shift)
print("Encrypted message is: " + encrypted_message)

# Decrypt
decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
print("Decrypted message is: " + decrypted_message)
