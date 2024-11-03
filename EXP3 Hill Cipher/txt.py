import numpy as np

def matrix_mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))
    print(f"Determinant: {det}")

    # Check if the determinant is coprime with the modulus
    if np.gcd(det, mod) != 1:
        raise ValueError("The determinant is not invertible under the given modulus.")

    det_inv = pow(det, -1, mod)
    print(f"Determinant Inverse: {det_inv}")

    matrix_adj = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    print(f"Adjugate Matrix: \n{matrix_adj}")

    inverse_matrix = (det_inv * matrix_adj) % mod
    print(f"Inverse Matrix (mod {mod}): \n{inverse_matrix}")
    return inverse_matrix

def text_to_matrix(text, size):
    text = text.upper().replace(" ", "")
    if len(text) % size != 0:
        text += 'X' * (size - len(text) % size)
    
    print(f"Padded Text: {text}")
    matrix = np.array([ord(c) - ord('A') for c in text]).reshape(-1, size)
    print(f"Text to Matrix: \n{matrix}")
    return matrix

def matrix_to_text(matrix):
    text = ''.join(chr(int(num) + ord('A')) for num in matrix.flatten())
    print(f"Matrix to Text: {text}")
    return text

def hill_encrypt(plain_text, key_matrix):
    size = key_matrix.shape[0]
    plain_matrix = text_to_matrix(plain_text, size)
    print(f"Plain Matrix: \n{plain_matrix}")
    encrypted_matrix = (plain_matrix @ key_matrix) % 26
    print(f"Encrypted Matrix: \n{encrypted_matrix}")
    return matrix_to_text(encrypted_matrix)

def hill_decrypt(cipher_text, key_matrix):
    size = key_matrix.shape[0]
    cipher_matrix = text_to_matrix(cipher_text, size)
    print(f"Cipher Matrix: \n{cipher_matrix}")

    try:
        key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
    except ValueError as e:
        print(f"Matrix inversion error: {e}")
        return ""

    decrypted_matrix = (cipher_matrix @ key_matrix_inv) % 26
    print(f"Decrypted Matrix: \n{decrypted_matrix}")
    return matrix_to_text(decrypted_matrix)

def get_key_matrix(size):
    key_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            while True:
                try:
                    value = int(input(f"Enter element [{i+1}][{j+1}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        key_matrix.append(row)
    return np.array(key_matrix)

def main():
    size = int(input("Enter the size of the key matrix: "))
    if size <= 0:
        print("Matrix size must be positive.")
        return

    print("Enter the key matrix:")
    key_matrix = get_key_matrix(size)
    print(f"Key Matrix: \n{key_matrix}")

    plain_text = input("Enter the plain text: ")
    print("Original Text:", plain_text)

    encrypted_text = hill_encrypt(plain_text, key_matrix)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = hill_decrypt(encrypted_text, key_matrix)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
'''Enter the size of the key matrix: 2
Enter the key matrix:
Enter element [1][1]: 9
Enter element [1][2]: 4
Enter element [2][1]: 5
Enter element [2][2]: 7
Key Matrix: 
[[9 4]
 [5 7]]
Enter the plain text: exam
Original Text: exam
Padded Text: EXAM
Text to Matrix:
[[ 4 23]
 [ 0 12]]
Plain Matrix:
[[ 4 23]
 [ 0 12]]
Encrypted Matrix:
[[21 21]
 [ 8  6]]
Matrix to Text: VVIG
Encrypted Text: VVIG
Padded Text: VVIG
Text to Matrix:
[[21 21]
 [ 8  6]]
Cipher Matrix:
[[21 21]
 [ 8  6]]
Determinant: 43
Determinant Inverse: 23
Adjugate Matrix:
[[ 7 22]
 [21  9]]
Inverse Matrix (mod 26): 
[[ 5 12]
 [15 25]]
Decrypted Matrix:
[[ 4 23]
 [ 0 12]]
Matrix to Text: EXAM
Decrypted Text: EXAM '''