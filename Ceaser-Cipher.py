import string

alphabets = string.ascii_uppercase *2
encode_input =  "encrypt"
decode_input =  "decrypt"


def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    dir = "encrypting"
    # if the direction is valid, then make the shift amount negative
    if cipher_direction =='decrypt':
        dir = "decrypting"
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            # get the index
            index = alphabets.index(char)
            # shift the index
            new_index = index + shift_amount
            # add the alphabet at the given index to the end string
            end_text += alphabets[new_index]
        else:
            # if the char is not an alphabet, then Error out
            print(f"\nText {start_text} contains non alphabets, Enter valid alphabets. \n")
    if cipher_direction =='decrypt':
        print(f"\n PlainText after {dir} is: {end_text}\n")
    else:
        print(f"\n Ciphertext after {dir} is: {end_text}\n")


should_continue = True
while should_continue:
    direction = input("Enter encrypt or decrypt: ")
    if not direction == 'encrypt' or direction == 'decrypt':
        print(f"{direction} is not a valid input.")
        continue
    text = input(f"\nEnter text to {direction}: ").upper()
    valid_text=text.replace(".","X").replace(" ",'')
    print (valid_text)
    if not valid_text.isalpha():
        print(f"\nText {text} contains non alphabets, Enter valid alphabets. \n")
        text = input(f"\nEnter text to {direction}: ").upper()
    shift = int(input("Enter the  cipher key - Only Numerics allowed: "))
    print (shift)
    caesar(direction, valid_text, shift)

    if input("Do you want to go again? (y/n): ").casefold() != "y":
        should_continue = False
        print("\nExiting.")
