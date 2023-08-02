def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure shift is within one full rotation of the alphabet
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plain_text = input("Please enter a sentence: ")
shift = int(input("Please enter the shift value: "))
encrypted_text = caesar_cipher(plain_text, shift)
print("The encrypted sentence is:", encrypted_text)