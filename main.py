import pyAesCrypt
from pathlib import Path

def process_file():
    """
    Asks the user whether they want to encrypt or decrypt a file, then prompts for the
    corresponding file path and password, and performs the specified action on the file.
    """
    action = ''
    while action.lower() not in ('e', 'd'):
        action = input("Do you want to encrypt or decrypt a file? Enter 'e' for encrypt or 'd' for decrypt: ")

        if action.lower() not in ('e', 'd'):
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

    file_path_input = input("Please enter the path to the file you want to " + ("encrypt: " if action.lower() == 'e' else "decrypt: "))
    file_path = Path(file_path_input)

    if not file_path.exists():
        print(f"The file {file_path} does not exist. Please check the path and try again.")
        return

    password = input("Enter the password for " + ("encrypting" if action.lower() == 'e' else "decrypting") + " the file: ")

    if action.lower() == 'e':
        encrypted_file_path = file_path.with_suffix('.aes')
        print(f"Encrypting {file_path} to {encrypted_file_path}...")
        pyAesCrypt.encryptFile(str(file_path), str(encrypted_file_path), password)
        print("Encryption complete.")
    elif action.lower() == 'd':
        decrypted_file_path = file_path.with_name(file_path.stem + '1.txt')
        print(f"Decrypting {file_path} to {decrypted_file_path}...")
        pyAesCrypt.decryptFile(str(file_path), str(decrypted_file_path), password)
        print("Decryption complete.")

if __name__ == "__main__":
    process_file()
