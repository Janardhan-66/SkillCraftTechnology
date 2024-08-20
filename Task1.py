def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice.lower() == 'e':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice.lower() == 'd':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
