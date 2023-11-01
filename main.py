# louis lee

def printMenu():
    print("\nMenu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


def encode(num):
    encodedPassword = ""
    for digit in num:
        digitShift = str((int(digit) + 3) % 10)
        encodedPassword += digitShift

    return encodedPassword


def decode(num):  # Kai Vedder
    decodedPassword = ""
    for digit in num:
        print(digit)
        decodedPassword += str((int(digit) - 3) % 10)
    return decodedPassword


def main():
    MenuOn = True
    while MenuOn:
        printMenu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = str(input("Please enter your password to encode: "))
            encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print("The encoded password is " + encode(password) + ", and the original password is " + password + ".")
        else:
            MenuOn = False


if __name__ == "__main__":
    main()
