clear_Text1 = "To those friends conspiring against all humanity"
clear_Text2 = "Undoing codes ultmately wears down corrupted hacker fools!"

# split the stirng with the space as the delimiter
splited_Text1 = clear_Text1.split(" ")
splited_Text2 = clear_Text2.split(" ")

nCount = 0


# print the first letter of each word
for word in splited_Text1:
    print(word[nCount])
    nCount += 1