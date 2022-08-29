from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def ceasar(direction_choice, message, shift_count):
    if direction_choice == "encode":
        cipher_text = ""
        for char in message:
            if char not in alphabet:
                cipher_text += char
            else:
                index = alphabet.index(char)
                shifted_alphabet = index + shift_count
                cipher_text += alphabet[shifted_alphabet]
        print(f"The encoded text is: {cipher_text}")
    elif direction_choice == "decode":
        decrypt_text = ""
        for char in message:
            if char not in alphabet:
                decrypt_text += char
            else:
                index = alphabet.index(char)
                unshifted_alphabet = index - shift_count
                decrypt_text += alphabet[unshifted_alphabet]
        print(f"The decoded text is: {decrypt_text}")



print(logo)
restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(direction_choice=direction, message=text, shift_count=shift)

    restart_program = input("Do you want to restart? Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if restart_program == "no":
        restart = False
    else:
        restart = True
