def load_image(file_path):
    with open(file_path, 'rb') as f:
        return bytearray(f.read())

def save_image(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)

def encrypt_image(image_data):
    # Create a copy to avoid modifying the original image
    encrypted_data = image_data[:]

    # Simple encryption: XOR each byte with a key (e.g., 42) and swap pixels
    key = 42
    for i in range(0, len(encrypted_data), 3):
        # XOR operation with the key
        encrypted_data[i] ^= key
        if i + 1 < len(encrypted_data):
            encrypted_data[i + 1] ^= key
        if i + 2 < len(encrypted_data):
            encrypted_data[i + 2] ^= key

        # Swap first and last bytes in each RGB triplet
        if i + 2 < len(encrypted_data):
            encrypted_data[i], encrypted_data[i + 2] = encrypted_data[i + 2], encrypted_data[i]

    return encrypted_data

def decrypt_image(encrypted_data):
    # Reverse the encryption steps
    decrypted_data = encrypted_data[:]

    key = 42
    for i in range(0, len(decrypted_data), 3):
        # Swap first and last bytes in each RGB triplet back to original
        if i + 2 < len(decrypted_data):
            decrypted_data[i], decrypted_data[i + 2] = decrypted_data[i + 2], decrypted_data[i]

        # Reverse the XOR operation with the key
        decrypted_data[i] ^= key
        if i + 1 < len(decrypted_data):
            decrypted_data[i + 1] ^= key
        if i + 2 < len(decrypted_data):
            decrypted_data[i + 2] ^= key

    return decrypted_data

# Paths to the image files
input_image_path = 'your_image.bmp'
encrypted_image_path = 'encrypted_image.bmp'
decrypted_image_path = 'decrypted_image.bmp'

# Load the image
image_data = load_image(input_image_path)

# Encrypt the image
encrypted_data = encrypt_image(image_data)

# Save the encrypted image
save_image(encrypted_image_path, encrypted_data)

# Decrypt the image
decrypted_data = decrypt_image(encrypted_data)

# Save the decrypted image
save_image(decrypted_image_path, decrypted_data)

print("Image encryption and decryption complete.")
