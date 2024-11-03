from PIL import Image

def encrypt_image(original_image, key):
    try:
        encrypted_image = original_image.copy()
        original_pixels = original_image.load()
        encrypted_pixels = encrypted_image.load()
        width, height = encrypted_image.size
        
        for i in range(width):
            for j in range(height):
                current_pixel_value = original_pixels[i, j]
                encrypted_pixel = tuple((val + key) % 256 for val in current_pixel_value)
                encrypted_pixels[i, j] = encrypted_pixel 

        return encrypted_image
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def decrypt_image(encrypted_image, key):
    try:
        decrypted_image = encrypted_image.copy()
        encrypted_pixels = encrypted_image.load()
        decrypted_pixels = decrypted_image.load()
        width, height = decrypted_image.size
        
        for i in range(width):
            for j in range(height):
                current_pixel_value = encrypted_pixels[i, j]
                decrypted_pixel = tuple((val - key) % 256 for val in current_pixel_value)
                decrypted_pixels[i, j] = decrypted_pixel
        
        return decrypted_image
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    input_image_path = 'E:\\CNS YAKSH\\EXP1 Shiftcipher\\img.png'
    key = int(input("Enter the shift key (integer): "))
    encrypted_image_path = 'E:\\CNS YAKSH\\EXP1 Shiftcipher\\encrypted_image.jpg'
    decrypted_image_path = 'E:\\CNS YAKSH\\EXP1 Shiftcipher\\decrypted_image.jpg'

    try:
        original_image = Image.open(input_image_path)
        encrypted_image = encrypt_image(original_image, key)
        
        if encrypted_image:
            encrypted_image.save(encrypted_image_path)
            print(f"Encrypted image saved as {encrypted_image_path}")
            
            decrypted_image = decrypt_image(encrypted_image, key)
            if decrypted_image:
                decrypted_image.save(decrypted_image_path)
                print(f"Decrypted image saved as {decrypted_image_path}")
            else:
                print("Decryption failed.")
        else:
            print("Encryption failed.")
    except Exception as e:
        print(f"Error processing the image: {str(e)}")

if __name__ == "__main__":
    main()
