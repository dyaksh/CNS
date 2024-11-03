import time
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(plaintext, key, iv):
    des_cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = des_cipher.encrypt(pad(plaintext, DES.block_size))
    return ciphertext

def des_decrypt(ciphertext, key, iv):
    des_cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext_decrypted = unpad(des_cipher.decrypt(ciphertext), DES.block_size)
    return plaintext_decrypted

def demonstrate_avalanche_effect():
    # Initial values
    key = b'EightBit'
    plaintext = b'123456'

    # Encryption
    print(f'Plain text = {plaintext}')
    init_vector = get_random_bytes(DES.block_size)
    print(f'Key = {key}')
    
    stime = time.time()
    ciphertext = des_encrypt(plaintext, key, init_vector)
    print(f'Ciphertext: {ciphertext}')
    etime = time.time()
    print(f'Encryption Time = {etime - stime:.6f} seconds')

    # Decryption
    decrypted_text = des_decrypt(ciphertext, key, init_vector)
    print(f'Decrypted Plaintext: {decrypted_text}')
    print(f'Decryption Time = {time.time() - etime:.6f} seconds\n')

    # Avalanche Effect 1 - Change in plaintext
    plaintext = b'122456'
    print(f'Plain text = {plaintext}')
    init_vector = get_random_bytes(DES.block_size)
    print(f'Key = {key}')
    
    ciphertext = des_encrypt(plaintext, key, init_vector)
    print(f'Ciphertext: {ciphertext}')
    
    decrypted_text = des_decrypt(ciphertext, key, init_vector)
    print(f'Decrypted Plaintext: {decrypted_text}\n')

    # Avalanche Effect 2 - Change in key
    plaintext = b'123456'
    print(f'Plain text = {plaintext}')
    init_vector = get_random_bytes(DES.block_size)
    key = b'EightBin'  # Intentionally altered key
    print(f'Key = {key}')
    
    ciphertext = des_encrypt(plaintext, key, init_vector)
    print(f'Ciphertext: {ciphertext}')
    
    decrypted_text = des_decrypt(ciphertext, key, init_vector)
    print(f'Decrypted Plaintext: {decrypted_text}')

if __name__ == "__main__":
    demonstrate_avalanche_effect()
