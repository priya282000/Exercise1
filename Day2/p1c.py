try:
    file = open('C:\\Users\\padmapriya\\Documents\\stringOperations.txt', 'r')
    #Word repeated maximum number of times
    read_file=file.read().lower().split();
    max=0
    count=0
    temp=""
    for word in read_file:
        count=read_file.count(word)
        if max<count:
            max=count
            temp=word
    print(temp)

except IOError:
    print("File not found")