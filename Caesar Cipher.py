alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plainText, shiftAmount):
    codedText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        newLetter = alphabet[newPosition]
        codedText += newLetter
    print(f"The encoded text is {codedText}")

def decrypt(plainText, shiftAmount):
    decodedText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmount
        decodedText += alphabet[newPosition]
    print(f"The decoded text is {decodedText}")
    
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)