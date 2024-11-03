import numpy as np
import random
from PIL import Image

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self.find_coprime(self.phi)
        self.d = modinv(self.e, self.phi)

    def find_coprime(self, phi):
        e = 3
        while gcd(e, phi) != 1:
            e += 2
        return e

    def encrypt(self, plaintext):
        return [pow(byte, self.e, self.n) for byte in plaintext]

    def decrypt(self, ciphertext):
        return [pow(c, self.d, self.n) for c in ciphertext]

if __name__ == "__main__":
    p = 61  # Example prime number
    q = 53  # Example prime number
    rsa = RSA(p, q)

    # Load the image
    img = Image.open("img.jpg").convert("RGB")
    img_data = np.array(img)

    # Flatten pixel values and convert to list of ASCII values
    pixel_values = img_data.flatten().tolist()

    # Encrypt the pixel values
    ciphertext = rsa.encrypt(pixel_values)
    print("Ciphertext:", ciphertext)

    # Ensure the encrypted data fits within image pixel range
    encrypted_image_data = np.clip(np.array(ciphertext) % 256, 0, 255)
    img_shape = img_data.shape

    # Reshape and create the encrypted image
    encrypted_image = Image.fromarray(encrypted_image_data.astype(np.uint8).reshape(img_shape))
    encrypted_image_path = "./encrypted_image.png"
    encrypted_image.save(encrypted_image_path)

    # Decrypt the image data
    decrypted_data = rsa.decrypt(ciphertext)
    decrypted_pixel_values = np.array(decrypted_data).reshape(img_shape)

    # Create the decrypted image
    decrypted_image = Image.fromarray(decrypted_pixel_values.astype('uint8'), 'RGB')
    decrypted_image_path = "./decrypted_image.png"
    decrypted_image.save(decrypted_image_path)

    print(f"Encrypted image saved as '{encrypted_image_path}'")
    print(f"Decrypted image saved as '{decrypted_image_path}'")
