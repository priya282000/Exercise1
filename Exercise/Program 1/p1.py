try:
    get_file=open('C:\\Users\\padmapriya\\Documents\\sampl.txt','r')
    read_file=get_file.read()
    get_words=read_file.split()
    unique_words=set(get_words)
    l=[]
    for word in unique_words:
        l.append(word)
    print(sorted(l,key=len))
except IOError:
    print("File not found")
except Exception as e:
    print(e)

