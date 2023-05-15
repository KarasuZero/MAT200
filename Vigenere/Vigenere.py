# encrypt and decrypt a message using the Vigenere cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"

def count_letters(msg):
    letter_count = 0
    for char in msg:
        if char.isalpha():
            letter_count += 1

    return letter_count


def vigenere_encrypt(key, plaintext):
    ciphertext = ''
    key_idx = 0

    for char in plaintext:
        # if the character is a letter, shift it
        if char.isalpha():
            # find the shift amount by finding the index of the key character in the alphabet and subtracting 65 (the ASCII value of 'A')
            shift = ord(key[key_idx % len(key)]) - 65

            # shift the character by the shift amount
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)

            # add the shifted character to the ciphertext
            ciphertext += shifted_char
            key_idx += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(key, ciphertext):
    plaintext = ''
    key_idx = 0

    # loop through the ciphertext
    for char in ciphertext:
        if char.isalpha():

            # find the shift amount by finding the index of the key character in the alphabet and subtracting 65 (the ASCII value of 'A')
            shift = ord(key[key_idx % len(key)]) - 65

            # print the shifted alphabet based on the shift amount
            # shifted_alphabet = alphabet[shift:] + alphabet[:shift]
            # print(shifted_alphabet)

            # shift the character by the shift amount
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)

            # add the shifted character to the plaintext
            plaintext += shifted_char
            key_idx += 1

        else:
            plaintext += char

    return plaintext



key = "MATHEMAGICIAN"
msg = "NOW TRANSPOSE THE DIGITS ANY WAY YOU WISH. USING THE ORIGINAL FOUR DIGIT NUMBER AND THIS NEW TRANSPOSE, SUBTRACT THE SMALLER FOUR DIGIT NUMBER FROM THE LARGER ONE."
ciphertext = "TEKL ME A LCP TIGFLX UYYBKZ TQDQXE YVV KOA BQ BRL: NEZPR NY CZKBIAS DHDR FHK TCAT SAUK KMSIZA QN YBGR MLPQPNWPM NHYBXY."

# decrypt the ciphertext
plaintext = vigenere_decrypt(key, ciphertext)

#encrypt the plaintext
# ciphertext = vigenere_encrypt(key, plaintext)

# print(ciphertext)
print(plaintext)
