import hashlib
import time

# Function to compute MD5 hash
def hash_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

# Function to compute SHA-512 hash
def hash_sha512(data):
    return hashlib.sha512(data.encode()).hexdigest()

# Function to measure the time taken to hash the data
def measure_time(hash_func, data):
    start_time = time.time()
    hash_value = hash_func(data)
    end_time = time.time()
    return hash_value, end_time - start_time

# Test messages
messages = {
    "short": "Hi",
    "moderate": (
        "Security Threats. Computer systems face a number of security threats. "
        "One of the basic threats is data loss, which means that parts of a database can no longer be retrieved. "
        "This could be the result of physical damage to the storage medium (like fire or water damage), "
        "human error or hardware failures."
    ),
    "long": (
        "Instructor: Paul Zandbergen. Paul has a PhD from the University of British Columbia and has taught "
        "Geographic Information Systems, statistics and computer programming for 15 years. "
        "Computer systems face a number of security threats. Learn about different approaches to system security, "
        "including firewalls, data encryption, passwords and biometrics. "
        "Security Threats. Computer systems face a number of security threats. "
        "One of the basic threats is data loss, which means that parts of a database can no longer be retrieved. "
        "This could be the result of physical damage to the storage medium (like fire or water damage), "
        "human error or hardware failures. Another security threat is unauthorized access..."
    )
}

# Dictionary to store results
results = {}

# Measure performance
for size, message in messages.items():
    md5_hash, md5_time = measure_time(hash_md5, message)
    sha512_hash, sha512_time = measure_time(hash_sha512, message)
    results[size] = {
        "MD5": {"hash": md5_hash, "time": md5_time},
        "SHA-512": {"hash": sha512_hash, "time": sha512_time}
    }

# Print results
print("Comparison of MD5 and SHA-512:")
print("Criteria\t\tMD5\t\t\tSHA-512")
print("Input Size\t\tVaries\t\t\tVaries")
print("Output Size\t\t128 bits (32 hex chars)\t512 bits (128 hex chars)")
print("Time taken for short msg (\"Hi\"):\t{:.10f}s\t{:.10f}s".format(results['short']['MD5']['time'], results['short']['SHA-512']['time']))
print("Time taken for moderate msg:\t\t{:.10f}s\t{:.10f}s".format(results['moderate']['MD5']['time'], results['moderate']['SHA-512']['time']))
print("Time taken for long msg:\t\t{:.10f}s\t{:.10f}s".format(results['long']['MD5']['time'], results['long']['SHA-512']['time']))

# Analyze avalanche effect
print("\nAvalanche Effect Analysis:")
messages_to_test = [("Hi", "Ho"), ("CSS", "DSS")]
for msg1, msg2 in messages_to_test:
    hash1_md5 = hash_md5(msg1)
    hash2_md5 = hash_md5(msg2)
    hash1_sha512 = hash_sha512(msg1)
    hash2_sha512 = hash_sha512(msg2)
    print(f"Changing '{msg1}' to '{msg2}':")
    print(f"MD5: {hash1_md5} -> {hash2_md5}")
    print(f"SHA-512: {hash1_sha512} -> {hash2_sha512}")
    print("---")

# Comments on message digest lengths
print("\nMessage Digest Lengths:")
print("MD5 digest length: 128 bits (32 hex characters)")
print("SHA-512 digest length: 512 bits (128 hex characters)")

# Note: The remaining parts of your analysis (collisions, original message retrieval, etc.) require further research.

