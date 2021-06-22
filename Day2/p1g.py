import re

#split the words based on vowels
try:
    def split_vowels():
        rf = open('C:\\Users\\padmapriya\\Documents\\test.txt', 'r')
        read_content = rf.read()
        return (re.sub(r"(\w)([a,e,i,o,u,A,E,I,O,U])", r"\1 \2", read_content))
except IOError:
    print("File not found")


#capitalise 3rd letter of each word
try:
    def capitalise():
        rf = open('C:\\Users\\padmapriya\\Documents\\test.txt', 'r')
        read_content = rf.read().split()
        str=''
        for word in read_content:
            temp=word
            if len(word)>3:
                temp=word[:2]+word[2].upper()+word[3:]
            if len(word)==3:
                temp=word[:2]+word[2].upper()
            str=str+' '+temp

        return str
except IOError:
    print("File not found")


#replace whitespaces with -
try:
    def replace_whitespace():
        rf = open('C:\\Users\\padmapriya\\Documents\\test.txt', 'r')
        read_content = rf.read().split()
        str=''
        for word in read_content:
            str=str+word+'-'
        return str
except IOError:
    print("File not found")

#use semi colon for new line
try:
    def replace_semicolon():
        f=open('C:\\Users\\padmapriya\\Documents\\test.txt','r')
        read_content=f.read().split('.')
        str=''
        for line in read_content:
            str=str+line+';\n'
        return str
except IOError:
    print("File not found")


try:
    f=open('C:\\Users\\padmapriya\\Documents\\test.txt','w')
    l='Python is a high level interpreted interactive and object oriented scripting language.Python is designed to be highly readable.It uses English keywords frequently where as other languages use punctuation and it has fewer syntactical constructions than other languages'
    f.write(l)
    f.seek(0)
    f.write(split_vowels())
    f.seek(0)
    f.write(capitalise())
    f.seek(0)
    f.write(replace_whitespace())
    f.seek(0)
    f.write(replace_semicolon())
    f.close()
except IOError:
    print("File not found")