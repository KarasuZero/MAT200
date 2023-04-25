alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_info(key, shifted_alphabet):
    print("key: " + str(key))

    print("alphabet: " + alphabet)

    print("shifted_alphabet: " + shifted_alphabet)


def caesar_encrypt(key, msg):
    # shift the alphabet by the key mod 26
    shifted_alphabet = alphabet[key % 26:] + alphabet[:key % 26]

    print_info(key, shifted_alphabet)

    # loop through the message and encrypt each letter
    for letter in msg:
        # find the index of the letter in the alphabet
        index = alphabet.find(letter)

        # if the letter is not in the alphabet, add it to the ciphertext
        if index == -1:
            print(letter, end='')
        else:
            # use the index to find the letter in the shifted alphabet
            print(shifted_alphabet[index], end='')

    print("\n")


def caesar_decrypt(key, msg):
    # shift the alphabet by the key mod 26
    shifted_alphabet = alphabet[key % 26:] + alphabet[:key % 26]

    print_info(key, shifted_alphabet)

    print("Decrypted:")
    # loop through the message and decrypt each letter
    for letter in msg:
        # find the index of the letter in the shifted alphabet
        index = shifted_alphabet.find(letter)

        # if the letter is not in the alphabet, add it to the plaintext
        if index == -1:
            print(letter, end='')

        else:
            # use the index to find the letter in the alphabet
            print(alphabet[index], end='')
    print("\n")


def caesar_decrypt_crack(msg):
    key = 25
    while key >= 1:
        caesar_decrypt(key, msg)
        key -= 1



data ="JUT'Z YCKGZ ZNK VKZZE ZNOTMY, GTJ JUT'Z VKZ ZNK YCKGZE ZNOTMY"

# print("Encryption:\n")
# caesar_encrypt(10, data)
#
# print("Decryption:\n")
# caesar_decrypt(19, data)
#
print("Crack:\n")
caesar_decrypt_crack(data)
