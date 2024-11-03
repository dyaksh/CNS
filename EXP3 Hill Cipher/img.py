import numpy as np
from PIL import Image

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_block(block, key_matrix):
    return np.dot(key_matrix, block) % 256

def decrypt_block(block, inv_key_matrix):
    return np.dot(inv_key_matrix, block) % 256

def hill_cipher_image(image_path, key_matrix, mode='encrypt'):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)

    n = key_matrix.shape[0]

    if mode == 'decrypt':
        det = int(np.round(np.linalg.det(key_matrix)))
        det_inv = mod_inverse(det, 256)

        if det_inv is None:
            raise ValueError("Key matrix is not invertible under mod 256")

        adjugate_matrix = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 256
        inv_key_matrix = (det_inv * adjugate_matrix) % 256
    else:
        inv_key_matrix = None

    encrypted_pixels = pixels.copy()

    for i in range(0, pixels.shape[0] - n + 1, n):
        for j in range(0, pixels.shape[1] - n + 1, n):
            for k in range(3):  # Iterate over R, G, B channels
                block = pixels[i:i+n, j:j+n, k].reshape(n, n)

                if mode == 'encrypt':
                    encrypted_block = encrypt_block(block, key_matrix)
                else:
                    encrypted_block = decrypt_block(block, inv_key_matrix)

                # Ensure block is correctly reshaped back into the image
                encrypted_pixels[i:i+n, j:j+n, k] = encrypted_block.reshape(n, n)

    encrypted_img = Image.fromarray(encrypted_pixels.astype(np.uint8))
    output_path = image_path.split('.')[0] + ('_encrypted' if mode == 'encrypt' else '_decrypted') + '.png'
    encrypted_img.save(output_path)

    return output_path

# Define key matrix
key_matrix = np.array([[2, 9, 1, 4], 
                       [5, 4, 8, 3], 
                       [5, 2, 7, 1], 
                       [1, 6, 3, 8]])

# Path to the image file (make sure this file exists)
image_path = r'C:\Users\djsce.student\Desktop\CNS YAKSH\nature.jpeg'

# Encrypt image
encrypted_image_path = hill_cipher_image(image_path, key_matrix, mode='encrypt')
print(f"Encrypted image saved to: {encrypted_image_path}")

# Decrypt image
decrypted_image_path = hill_cipher_image(encrypted_image_path, key_matrix, mode='decrypt')
print(f"Decrypted image saved to: {decrypted_image_path}")
