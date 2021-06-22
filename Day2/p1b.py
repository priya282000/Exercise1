try:
    file = open('C:\\Users\\padmapriya\\Documents\\stringOperations.txt', 'r')
    #number of words ending with 'ing'
    count=0
    for word in file.read().split():
        if word.endswith('ing'):
            count+=1
    print("Number of words ending with 'ing' in the file :",count)
    file.close()
except IOError:
    print("File not found")
except Exception as e:
    print(e)

