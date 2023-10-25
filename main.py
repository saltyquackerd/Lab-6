# Hailey Lin
def encode(pwd): # encodes the password
    encoded = ""

    for i in pwd:
        encoded += str((int(i) + 3) % 10)

    return encoded

def decode(pwd): #decodes the password
    decoded = ""

    for i in pwd:
        decoded += str((int(i) - 3) % 10)

    return decoded

if __name__ == "__main__":
    encoded_password = ""

    while True:
        # print the menu options
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_op = int(input("Please enter an option: "))

        if menu_op == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif menu_op == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
        elif menu_op == 3:
            break

