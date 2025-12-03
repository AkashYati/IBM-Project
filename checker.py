# Smart Password Strength Checker
print("---- Password Strength Checker ----")
print("Type 'exit' to stop.\n")

while True:
    pwd = input("Enter a password to check: ")
    if pwd.lower() == "exit":
        break

    strength = 0
    
    if len(pwd) >= 8:
        strength += 1
    if any(c.isupper() for c in pwd):
        strength += 1
    if any(c.islower() for c in pwd):
        strength += 1
    if any(c.isdigit() for c in pwd):
        strength += 1
    if any(not c.isalnum() for c in pwd):
        strength += 1

    print("Strength:", end=" ")

    if strength == 5:
        print("Very Strong 🔥💪")
    elif strength == 4:
        print("Strong 💪")
    elif strength == 3:
        print("Medium 🙂")
    elif strength == 2:
        print("Weak ⚠️")
    else:
        print("Very Weak ❌")

    print()