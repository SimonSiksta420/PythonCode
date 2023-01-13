from cgitb import text


text = input("Zadej text: ")
key = int(input("Zadej klíč: "))

def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

input("Zašifrovaný text: " + encrypt(text, key))