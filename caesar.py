def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    
    for char in plain_text:
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        if char.isupper():
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    
    return decrypted_text

def main():
    print("Caesar Cipher Encryption and Decryption")
    
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value (positive for encryption, negative for decryption): "))
    
    encrypted_message = caesar_encrypt(message, shift_value)
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = caesar_decrypt(encrypted_message, shift_value)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
