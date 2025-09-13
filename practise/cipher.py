# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
#     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#     's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]


# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(text, shift):
#     cypher_text = ""
#     for char in text:
#         if char in alphabet:
#             original_position = alphabet.index(char)
#             cypher_position = (original_position + shift) % len(alphabet)  
#             cypher_text += alphabet[cypher_position]
#         else:
#             cypher_text += char  # keep spaces/punctuation as is
#     print(f"Encoded text: {cypher_text}")

# def decrypt(text, shift):
#     cypher_text = ""
#     for char in text:
#         if char in alphabet:
#             original_position = alphabet.index(char)
#             cypher_position = (original_position - shift) % len(alphabet)  
#             cypher_text += alphabet[cypher_position]
#         else:
#             cypher_text += char  # keep spaces/punctuation as is
#     print(f"decoded text: {cypher_text}")



# # Decide which function to run
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Invalid choice, please type 'encode' or 'decode'.")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encypt_decrypt(text, shift, direction):
    if direction not in ["encode", "decode"]:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        return   # exit the function early

    cypher_text = ""
    
    if direction == "decode":
        shift *= -1  # reverse the shift for decoding

    for char in text:
        if char in alphabet:
            original_position = alphabet.index(char)
            cypher_position = (original_position + shift) % len(alphabet)  
            cypher_text += alphabet[cypher_position]
        else:
            cypher_text += char  # keep spaces/punctuation unchanged

    print(f"Here is the {direction}d text: {cypher_text}")

continue_program = True
encypt_decrypt(text, shift, direction)

while continue_program:
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != 'yes':
        continue_program = False
        print("Thanks for playing")
    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

