import os
letters = list('abcdefghijklmnopqrstuvwxyz')

# Encryption function
def encrypt(message, shift):
    message = message.lower()
    result = ""
    for char in message:
        if char in letters:
            index = letters.index(char)
            shifted_index = (index + shift) % 26
            result += letters[shifted_index]
        else:
            result += char
    return result

# Decryption function
def decrypt(message, shift):
    return encrypt(message, -shift)

# Clear screen f
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main program loop
def main():
    while True:
        clear_screen()
        print("======= Caesar Cipher Tool =======")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        print("==================================")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            msg = input("\nEnter message to encrypt: ")
            try:
                shift = int(input("Enter shift value: "))
                encrypted = encrypt(msg, shift)
                print("\nEncrypted Message:", encrypted)
            except ValueError:
                print("Invalid shift value! It must be a number.")
        elif choice == '2':
            msg = input("\nEnter message to decrypt: ")
            try:
                shift = int(input("Enter shift value used during encryption: "))
                decrypted = decrypt(msg, shift)
                print("\nDecrypted Message:", decrypted)
            except ValueError:
                print("Invalid shift value! It must be a number.")
        elif choice == '3':
            print("Thank you for using Caesar Cipher Tool!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

        input("\nPress Enter to continue...")

# To run the program
main()
