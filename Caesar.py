message = input("Enter your message: ")
shift = int(input("Enter shift number: "))
mode = input("'d' for decryption and 'e' for encryption: ")

result = ""

for char in message:
    if char.isalpha():
        if char.isupper():
            base = 65
        else:
            base = 97

        if mode == "e":
            new_char = chr((ord(char) - base + shift) % 26 + base)
        elif mode == "d":
            new_char = chr((ord(char) - base - shift) % 26 + base)
        else:
            print("Invalid mode")
            break

        result += new_char
    else:
        result += char

print("Result:", result)