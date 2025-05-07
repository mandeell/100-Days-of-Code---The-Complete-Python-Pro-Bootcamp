# TODO-1: Import and print the logo from art.py when the program starts.
import art
import string

print(art.logo)

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
space = " "
alphabet = list(letters + digits + symbols + space)



# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    original_text = original_text.strip()
    for letter in original_text:
        shift = shift_amount
        if encode_or_decode == "decode":
            shift = -shift_amount

        shifted_position = alphabet.index(letter) + shift
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    global restart_code
    restart_code = input("\nEnter 'yes' to go again otherwise enter 'no': \n")


# TODO-3: Can you figure out a way to restart the cipher program?
restart_code = 'yes'

while restart_code == 'yes':
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)




