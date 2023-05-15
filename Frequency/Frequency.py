import string
import collections
import enchant
import re
from itertools import permutations

# Define the ciphertext and initialize variables
ciphertext = "NLCCP NUTT IJ U WUAP KRUK IJ ETUXPO SIKR PIWRK TUFWP NUTTJ UBO LBP JAUTTPF KUFWPK LF LNGPCK NUTT CUTTPO U EUTTIBU. KRPFP UFP YLMF NUTTJ EPF KPUA UBO KRPX UFP AUOP LY U OIYYPFPBK CLTLF LF EUKKPFB KL OIJKIBWMIJR KRP NUTTJ LY LBP KPUA YFLA KRLJP LY KRP LKRPF KPUA."
word_count = 0

# Define the function to perform the brute force substitution cipher
def brute_force_substitution_cipher(ciphertext):
    my_dict = enchant.Dict("en_US")
    # Split the ciphertext into words
    words = re.findall(r'\b\w+\b', ciphertext)
    
    # Count the frequency of each letter in the ciphertext
    freq_dict = collections.Counter(char for char in ciphertext if char.isalpha())
    freq_order = ''.join(char[0] for char in freq_dict.most_common())
    
    # Generate a list of possible permutations based on the most common letters in the ciphertext
    possible_permutations = permutations(freq_order[:len(freq_order)])
    
    # Loop through each permutation of the alphabet
    for alphabet in possible_permutations:
        # Create a dictionary to map each letter in the ciphertext to a letter in the alphabet
        mapping = {}
        for i in range(26):
            mapping[string.ascii_uppercase[i]] = alphabet[i] if string.ascii_uppercase[i] in freq_order else string.ascii_uppercase[i]

        # Apply the mapping to the ciphertext
        plaintext = ""
        for char in ciphertext:
            if char in mapping:
                plaintext += mapping[char]
            else:
                plaintext += char
        # Split the plaintext into words
        plaintext_words = re.findall(r'\b\w+\b', plaintext)
        # Check if the plaintext words are in the English dictionary
        if all(enchant.Dict("en_US").check(word) for word in plaintext_words):
            # Print the deciphered text and the alphabet mapping
            print("Deciphered text: " + plaintext)
            print("Alphabet mapping: " + str(alphabet))
            break

# Count how many words there are in the ciphertext using spaces
for char in ciphertext:
    if char == " ":
        word_count += 1

# Print the number of words in the ciphertext
print("There are " + str(word_count) + " words in the ciphertext.")




# Perform the brute force substitution cipher
brute_force_substitution_cipher(ciphertext)
