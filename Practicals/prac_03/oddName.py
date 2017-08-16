name = input('Enter your name: ')
while name == "":
    print("Invalid name")
    name = input('Enter your name: ')
print([letter for i, letter in enumerate(name) if i % 2 == 1])