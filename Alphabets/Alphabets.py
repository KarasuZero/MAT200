alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_info(key, shifted_alphabet):
    print("\n")

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


def multiplicative_cipher_encrypt(msg, key):
    # Print out information about the encryption process
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    print_info(key, shifted_alphabet)

    # Encrypt the message
    encrypted_msg = ""
    for char in msg:
        if char in alphabet:
            char_idx = alphabet.index(char)
            encrypted_char_idx = (char_idx * key) % 26
            encrypted_msg += alphabet[encrypted_char_idx]
        else:
            encrypted_msg += char

    print(encrypted_msg)

    return encrypted_msg


def multiplicative_cipher_decrypt(msg, key):
    # Invert the key
    inverse_key = 0
    for i in range(1, 26):
        if (key * i) % 26 == 1:
            inverse_key = i
            break

    # Print out information about the decryption process
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    print_info(key, shifted_alphabet)

    # Decrypt the message
    decrypted_msg = ""
    for char in msg:
        if char in alphabet:
            char_idx = alphabet.index(char)
            decrypted_char_idx = (char_idx * inverse_key) % 26
            decrypted_msg += alphabet[decrypted_char_idx]
        else:
            decrypted_msg += char

    print(decrypted_msg)

    return decrypted_msg

def multiplicative_cipher_decrypt_crack(msg):
    for key in range(1, 26):
        multiplicative_cipher_decrypt(msg, key)


def affine_cipher_encrypt(msg, key1, key2):
    # Print out information about the encryption process
    shifted_alphabet = alphabet[key1:] + alphabet[:key1]
    print_info(key1, shifted_alphabet)

    # Encrypt the message
    encrypted_msg = ""
    for char in msg:
        if char in alphabet:
            char_idx = alphabet.index(char)
            encrypted_char_idx = ((char_idx * key1) + key2) % 26
            encrypted_msg += alphabet[encrypted_char_idx]
        else:
            encrypted_msg += char

    print(encrypted_msg)

    return encrypted_msg


def affine_cipher_decrypt(msg, key):
    # divide the key with 26 and separate the quotient and remainder
    key1 = key // 26
    key2 = key % 26

    # calculate the modular multiplicative inverse of key1
    inverse_key = 0
    for i in range(1, 26):
        if (key1 * i) % 26 == 1:
            inverse_key = i
            break

    # decrypt the message using the inverse key and key2
    decrypted_msg = ""
    for char in msg:
        if char.isalpha():
            char_idx = ord(char) - ord('A')
            decrypted_char_idx = (inverse_key * (char_idx - key2)) % 26
            decrypted_msg += chr(decrypted_char_idx + ord('A'))
        else:
            decrypted_msg += char

    # print information about the key and shifted alphabet
    shifted_alphabet = ""
    for i in range(26):
        shifted_char = chr(((i * inverse_key - key2) % 26) + ord('A'))
        shifted_alphabet += shifted_char
    print_info(key, shifted_alphabet)

    print(decrypted_msg)
    return decrypted_msg


# def affine_cipher_decrypt_crack(msg):
#     for key in range(1, 26 * 26):
#         affine_cipher_decrypt(msg, key)


data ="P JF DN HOJI P OZJMWZI JANLU EJMJOOZONHMJFD PW DRYNNO PWDUZJI NQ YNT UN IN UJKZD. PU'D MZJOOB RNFZ PW YJWIB ZJRY BZJM ILMPWH EJMJOOZONHMJF DZJDNW. "

# print("Encryption:\n")
# caesar_encrypt(10, data)
#
# print("Decryption:\n")
# caesar_decrypt(55, data)
#
# print("Crack:\n")
# caesar_decrypt_crack(data)
#
# print("Multiplicative Cipher Encryption:\n")
# multiplicative_cipher_encrypt(data, 23)
#
# print("Multiplicative Cipher Decryption:\n")
# multiplicative_cipher_decrypt(data, 23)
#
# print("Multiplicative Cipher Decryption Crack:\n")
# multiplicative_cipher_decrypt_crack(data)

# print("Affine Cipher Encryption:\n")
# affine_cipher_encrypt(data, 23, 5)

# print("Affine Cipher Decryption:\n")
# affine_cipher_decrypt_crack(data)
