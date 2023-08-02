def caesar_cipher(text):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) + 5)
        encrypted_text += encrypted_char
    return encrypted_text

plain_text = input("Please enter a sentence: ")
encrypted_text = caesar_cipher(plain_text)
print("The encrypted sentence is:", encrypted_text)
