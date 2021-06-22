try:
    file = open('C:\\Users\\padmapriya\\Documents\\stringOperations.txt', 'r')

    #convert the words into unique list
    read_file=set(file.read().split())
    l=list(read_file)
    print(l)
except IOError:
    print("File not found")