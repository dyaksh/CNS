import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key, iv):
    aes_cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = aes_cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def aes_decrypt(ciphertext, key, iv):
    aes_cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext_decrypted = unpad(aes_cipher.decrypt(ciphertext), AES.block_size)
    return plaintext_decrypted

def demonstrate_avalanche_effect():
    # Initial values
    key = b'MySecretPassword'
    plaintext = b'123456'

    # Encryption
    print(f'Plain text = {plaintext}')
    init_vector = get_random_bytes(AES.block_size)
    print(f'Key = {key}')
    
    stime = time.time()
    ciphertext = aes_encrypt(plaintext, key, init_vector)
    print(f'Ciphertext = {ciphertext}')
    etime = time.time()
    print(f'Encryption Time = {etime - stime:.6f} seconds')

    # Decryption
    decrypted_text = aes_decrypt(ciphertext, key, init_vector)
    print(f'Decrypted Text = {decrypted_text}')
    print(f'Decryption Time = {time.time() - etime:.6f} seconds\n')

    # Avalanche Effect 1 - Change in plaintext
    plaintext = b'122456'
    print(f'Plain text = {plaintext}')
    init_vector = get_random_bytes(AES.block_size)
    print(f'Key = {key}')
    
    ciphertext = aes_encrypt(plaintext, key, init_vector)
    print(f'Ciphertext = {ciphertext}')
    
    decrypted_text = aes_decrypt(ciphertext, key, init_vector)
    print(f'Decrypted Text = {decrypted_text}\n')

    # Avalanche Effect 2 - Change in key
    plaintext = b'123456'
    print(f'Plain text = {plaintext}')
    init_vector = get_random_bytes(AES.block_size)
    key = b'MySecretPasswotd'  # Intentionally altered key
    print(f'Key = {key}')
    
    ciphertext = aes_encrypt(plaintext, key, init_vector)
    print(f'Ciphertext = {ciphertext}')
    
    decrypted_text = aes_decrypt(ciphertext, key, init_vector)
    print(f'Decrypted Text = {decrypted_text}')

if __name__ == "__main__":
    demonstrate_avalanche_effect()
