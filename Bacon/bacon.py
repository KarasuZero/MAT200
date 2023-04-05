bacon_cipher = {
    'a': 'AAAAA', 'b': 'AAAAB', 'c': 'AAABA', 'd': 'AAABB', 'e': 'AABAA',
    'f': 'AABAB', 'g': 'AABBA', 'h': 'AABBB', ' i/j ': 'ABAAA',
    'k': 'ABAAB', 'l': 'ABABA', 'm': 'ABABB', 'n': 'ABBAA', 'o': 'ABBAB',
    'p': 'ABBBA', 'q': 'ABBBB', 'r': 'BAAAA', 's': 'BAAAB', 't': 'BAABA',
    ' u/v ': 'BAABB', 'w': 'BABAA', 'x': 'BABAB', 'y': 'BABBA',
    'z': 'BABBB'
}


def bacon_decode(ciphertext):
    plaintext = ''
    # split the ciphertext into blocks of 5
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = ciphertext.replace(',', '')
    ciphertext = ciphertext.replace('.', '')

    blocks = [ciphertext[i:i + 5] for i in range(0, len(ciphertext)-1, 5)]

    # loop through the blocks
    for block in blocks:
        print("Block: " + block)
        # find the sequence of the block
        sequence = ''
        for letter in block:
            # if the letter is uppercase, add a 'A' to the sequence
            if letter.isupper():
                sequence += 'A'
            # if the letter is lowercase, add a 'B' to the sequence
            elif letter.islower():
                sequence += 'B'

        print("Sequence: " + sequence)
        # use the dictionary to convert the sequence to a letter
        for key, value in bacon_cipher.items():
            if value == sequence:
                letter = key

                # add the letter to the plaintext
                plaintext += letter


    print("Plaintext: " + plaintext)
    return plaintext


def bacon_encode(plaintext, cipher_dict):
    ciphertext = ''
    for letter in plaintext:
        # use the dictionary to convert the letter to a binary sequence
        block = cipher_dict.get(letter.lower(), '')

        # add the encoded letter to the ciphertext
        ciphertext += block
    return ciphertext


def bacon_format(target_sentence, cipher):
    index = 0
    formattedText = ''
    #
    for letter in target_sentence:
        if cipher[index] == 'A':
            formattedText += letter.upper()
            index += 1

        elif cipher[index] == 'B':
            formattedText += letter.lower()
            index += 1

    return formattedText


# plainText = "TKDIIS NNIDH OOYT DWH IW A"
#
# print("Encoding")
# bacon_cipher = bacon_encode(plainText, bacon_cipher)
# print(bacon_cipher)
#
# sentence = "nordertodecryptthisandgetthemessagehiddenwithinyouwillneedtousebaconcipherstaircasecipherandreversecipher"
#
# print("Formatting")
# print(bacon_format(sentence, bacon_cipher))

print("Decoding")
cipherText = "n ORdER tO DeCRYpt ThIS ANd GET tHE MeSsaGE HidDEN wITHIN You WIll nEed To Use BacOn cIpHEr, STAIrcaSeCIPHer aNd REVeRsE CIPHER"

bacon_decode(cipherText)

print("The End")
