# Hailey Lin
def encode(pwd): # encodes the password
    encoded = ""

    for i in pwd:
        encoded += str((int(i) + 3) % 10)

    return encoded


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
            pass
        elif menu_op == 3:
            break

