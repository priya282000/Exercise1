try:
    file = open('C:\\Users\\padmapriya\\Documents\\stringOperations.txt', 'r')

    #find palindrome in the file
    read_file=set(file.read().lower().split())
    for word in read_file:
        rev=''.join(reversed(word))
        if word==rev:
            print(word)
except IOError:
    print("File not found")