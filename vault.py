# Smart Password Vault — Interactive Python Program

vault = {}
SHIFT = 4

def encrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) + SHIFT)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) - SHIFT)
    return result


while True:
    print("\n---- PASSWORD VAULT ----")
    print("1. Add Password")
    print("2. View Saved Passwords")
    print("3. Search Password by Account")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account = input("Enter account/website name: ")
        pwd = input("Enter password: ")
        vault[account] = encrypt(pwd)
        print("Password Saved Securely! 🔐")

    elif choice == "2":
        if not vault:
            print("Vault is empty!")
        else:
            print("\nSaved Passwords:")
            for acc, epwd in vault.items():
                print(f"{acc} → {decrypt(epwd)}")

    elif choice == "3":
        account = input("Enter account name to search: ")
        if account in vault:
            print("Password:", decrypt(vault[account]))
        else:
            print("Account not found.")

    elif choice == "4":
        account = input("Enter account to delete: ")
        if account in vault:
            del vault[account]
            print("Deleted successfully.")
        else:
            print("Account not found.")

    elif choice == "5":
        print("Exiting Password Vault…")
        break

    else:
        print("Invalid option! Try again.")