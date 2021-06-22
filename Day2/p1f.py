import collections

try:
    file = open('C:\\Users\\padmapriya\\Documents\\stringOperations.txt', 'r')
    read_file=file.read().split()
    counter=collections.Counter(read_file)
    print(counter)
except IOError:
    print("File not found")
except Exception as e:
    print(e)