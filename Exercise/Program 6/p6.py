try:
    character=input("Enter a character : ")
    if(len(character)>1):
        raise ValueError("Character length cannot be more than 1")
    print("ASCII value of",character,"is",ord(character))
except ValueError as e:
    print(e)
