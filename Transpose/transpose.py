import numpy as np


def print_matrix(matrix):
    print("-" * (len(matrix[0]) * 2 + 1))
    for row in matrix:
        temp = "|"
        for i in row:
            temp += i + "|"

        print(temp)
        print("-" * (len(matrix[0]) * 2 + 1))


def transposition_encrypt_key(key, data):
    print("data: " + data)
    data = data.replace(" ", "")
    data_len = len(data)

    print("input char length: " + str(data_len))

    # create a matrix based on the key
    if data_len % key != 0:
        data_len += key - data_len % key

    print("matrix length: " + str(data_len))

    matrix = np.array([["#"] * key] * (data_len // key))

    # fill the matrix with the data going row by row
    for i in range(data_len // key):
        for j in range(key):
            if i * key + j < len(data):
                matrix[i][j] = data[i * key + j]

    print_matrix(matrix)

    print("\nencrypted: ")
    output = ""
    for i in range(key):
        for j in range(data_len // key):
            if matrix[j][i] != "#":
                output += matrix[j][i]

    print(output)
    print("\n")


def transposition_decrypt_key(key, data):
    print("data: " + data)
    data = data.replace(" ", "")
    data_len = len(data)

    print("input char length: " + str(data_len))

    # temp string to hold empty spaces
    temp = "?" * data_len

    # add # to the end of the temp string if the data length is not divisible by the key
    if data_len % key != 0:
        temp += "#" * (key - data_len % key)

    # print("temp: " + temp)

    # create a matrix based on the key and temp string
    matrix = np.array(list(temp)).reshape(-1, key)

    # transpose the matrix
    matrix = matrix.transpose()

    # fill in the matrix with the data going row by row
    data_index = 0
    for row in range(key):
        for col in range(matrix.shape[1]):
            if matrix[row][col] != '#':
                if data_index < len(data):
                    matrix[row][col] = data[data_index]
                    data_index += 1

    print_matrix(matrix)

    # print decrypted data
    print("\ndecrypted: ")
    output = ""
    for col in range(matrix.shape[1]):
        for row in range(key):
            if matrix[row][col] != "#":
               output += matrix[row][col]

    print(output)
    print("\n")

def transposition_decrypt_crack(data, key_limit):
    key = key_limit
    while key > 2:
        print("key: " + str(key))
        transposition_decrypt_key(key, data)
        key -= 1

if __name__ == "__main__":
    key = 7
    data = "This is a simple encryption"

    transposition_encrypt_key(key, data)

    # transposition_decrypt_key(key, data)

    # transposition_decrypt_crack(data, 10)
