def create_matrix(key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = key.upper()
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix and char != 'J':
            matrix.append(char)
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix
 
def preprocess_text(text):
    text = text.upper()
    processed_text = ''
    for i in range(len(text)):
        if i > 0 and text[i] == text[i-1]:
            processed_text += 'X'
        processed_text += text[i]
    if len(processed_text) % 2 == 1:
        processed_text += 'Z'
    return processed_text
 
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)
 
def encrypt(matrix, text):
    encrypted_text = ''
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        pos1 = find_position(matrix, char1)
        pos2 = find_position(matrix, char2)
        if pos1[0] == pos2[0]:
            encrypted_text += matrix[pos1[0]][(pos1[1]+1)%5]
            encrypted_text += matrix[pos2[0]][(pos2[1]+1)%5]
        elif pos1[1] == pos2[1]:
            encrypted_text += matrix[(pos1[0]+1)%5][pos1[1]]
            encrypted_text += matrix[(pos2[0]+1)%5][pos2[1]]
        else:
            encrypted_text += matrix[pos1[0]][pos2[1]]
            encrypted_text += matrix[pos2[0]][pos1[1]]
    return encrypted_text
 
def decrypt(matrix, text):
    decrypted_text = ''
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        pos1 = find_position(matrix, char1)
        pos2 = find_position(matrix, char2)
        if pos1[0] == pos2[0]:
            decrypted_text += matrix[pos1[0]][(pos1[1]-1)%5]
            decrypted_text += matrix[pos2[0]][(pos2[1]-1)%5]
        elif pos1[1] == pos2[1]:
            decrypted_text += matrix[(pos1[0]-1)%5][pos1[1]]
            decrypted_text += matrix[(pos2[0]-1)%5][pos2[1]]
        else:
            decrypted_text += matrix[pos1[0]][pos2[1]]
            decrypted_text += matrix[pos2[0]][pos1[1]]
    return decrypted_text
 
def postprocess_text(text):
    text = text.replace('X', '')
    if text[-1] == 'Z':
        text = text[:-1]
    return text
 
def playfair_cipher(key, message):
    matrix = create_matrix(key)
    processed_text = preprocess_text(message)
    print("Processed Text:", processed_text)
    digraphs = [processed_text[i:i+2] for i in range(0, len(processed_text), 2)]
    print("Digraphs:", digraphs)
    encrypted_text = encrypt(matrix, processed_text)
    print("Encryption Output:")
    for i in range(0, len(processed_text), 2):
        char1 = processed_text[i]
        char2 = processed_text[i+1]
        pos1 = find_position(matrix, char1)
        pos2 = find_position(matrix, char2)
        if pos1[0] == pos2[0]:
            print(f"{char1}{char2} -> {encrypted_text[i]}{encrypted_text[i+1]} (Same row, shift columns)")
        elif pos1[1] == pos2[1]:
            print(f"{char1}{char2} -> {encrypted_text[i]}{encrypted_text[i+1]} (Same column, shift rows)")
        else:
            print(f"{char1}{char2} -> {encrypted_text[i]}{encrypted_text[i+1]} (Rectangle, swap corners)")
    decrypted_text = decrypt(matrix, encrypted_text)
    print("Decryption Output:", postprocess_text(decrypted_text))
 
playfair_cipher("RICE", "ATTACK")
 
 
 