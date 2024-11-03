import random
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_candidate(length):
    p = random.getrandbits(length)
    # Ensure the candidate is odd and has the highest bit set
    return p | (1 << (length - 1)) | 1

def generate_prime_number(length):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d_old, d_new = 1, 0
    r_old, r_new = e, phi
    while r_new != 0:
        quotient = r_old // r_new
        d_old, d_new = d_new, d_old - quotient * d_new
        r_old, r_new = r_new, r_old - quotient * r_new
    if r_old > 1:
        raise ValueError("e is not invertible.")
    if d_old < 0:
        d_old += phi
    return d_old

def generate_keys(bit_length=8):
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [(ord(char) ** e) % n for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr((char ** d) % n) for char in encrypted_message])
    return decrypted_message

def main():
    public_key, private_key = generate_keys(bit_length=8)

    print("Public Key:", public_key)
    print("Private Key:", private_key)
    message = input("Enter a message to encrypt (alphanumeric only): ")
    encrypted_message = encrypt(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")
    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
