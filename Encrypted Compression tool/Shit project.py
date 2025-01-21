import os

def caesar_encrypt(text, shift):
    encrypted = ""
    for character in text:
        if character.isalpha(): 
            if character.isupper(): 
                shift_base=ord('A')
            else:
                shift_base=ord('a')
            new_char = chr((ord(character) - shift_base + shift) % 26 + shift_base)
            encrypted+=new_char
        else:
            encrypted+=character
    return encrypted


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def run_length_encode(text):#Compress
    compressed = ""
    i=0
    while i<len(text):
        count= 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compressed += text[i] + str(count)
        i += 1
    return compressed

def run_length_decode(text):#Decpmpress
    decompressed = ""
    i = 0
    while i < len(text):
        character = text[i]
        count = ""
        i += 1
        while i < len(text) and text[i].isdigit():
            count += text[i]
            i += 1
        decompressed += character * int(count)
    return decompressed

def load_users():
    users = []
    if os.path.exists("users.txt"):
        file=open("users.txt", 'r')
        for line in file:
            username, password = line.strip().split(",")
            users.append([username, password])
        file.close()
    return users

def save_users(users):
    file= open("users.txt", 'w')
    for user in users:
        file.write(f"{user[0]},{user[1]}\n")

def register_user(users):
    username = input("Enter username: ")
    password = input("Set a password: ")
    users.append([username, password])
    save_users(users)
    print("User registered successfully.")

def login_user(users):#Login
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user[0] == username and user[1] == password:
            print("Login successful! Welcome, " ,username)
            return 1
    print("Invalid username or password!")
    return 0

def encrypt_and_compress(input_file, output_file, shift):#Encrypt and compress a text file.
    with open(input_file, 'r') as file:
        text = file.read()

    encrypted = caesar_encrypt(text, shift)
    compressed = run_length_encode(encrypted)

    with open(output_file, 'w') as file:
        file.write(compressed)

    print("File encrypted and compressed successfully: ", output_file)

def decrypt_and_decompress(input_file, output_file, shift): #Decrypt and decompress the content of a text file.
    file=open(input_file, 'r')
    text = file.read()
    file.close()

    decompressed = run_length_decode(text)
    decrypted = caesar_decrypt(decompressed, shift)

    file=open(output_file, 'w')
    file.write(decrypted)
    file.close()

    print("File decrypted and decompressed successfully: ", output_file)

def file_menu():
    while True:
        print("1. Encrypt and Compress")
        print("2. Decrypt and Decompress")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_file = input("Enter the input file path: ")
            output_file = input("Enter the output file path: ")
            shift = int(input("Enter the shift value for Caesar Cipher: "))
            if os.path.exists(input_file):
                encrypt_and_compress(input_file, output_file, shift)
            else:
                print("Input file does not exist.")
        elif choice == '2':
            input_file = input("Enter the input file path: ")
            output_file = input("Enter the output file path: ")
            shift = int(input("Enter the shift value for Caesar Cipher: "))
            if os.path.exists(input_file):
                decrypt_and_decompress(input_file, output_file, shift)
            else:
                print("Input file does not exist.")
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")


users = load_users()
print("Secure File Management System")
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        register_user(users)
    elif choice == '2':
        if login_user(users):
            file_menu()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
            print("Invalid choice. Try again.")