try:
    file=open('C:\\Users\\padmapriya\\Documents\\stringOperations.txt','r')

    #number of words starting with prefix 'To'
    count=0
    for word in file.read().split():
        lower=word.lower()
        if lower.startswith('to'):
            count+=1
    print("Number of words having prefix 'To' in the file :",count)
    file.close()
except IOError:
    print("File not found")
except Exception as e:
    print(e)

