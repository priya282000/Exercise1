import collections
import logging
import re
import configfile as con
logging.basicConfig(filename='file.log', level=logging.INFO, format='%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')

class ReadWrite(object):
    def __init__(self,rf):
        self.rf=rf

    def readFile(self):
        try:
            f = open(self.rf,'r')
            read_content=f.read()
            return read_content
        except:
            logging.info("File not found")

    def writeFile(self,out):
        try:
            f = open(out, 'w')
            return f
        except:
            logging.info("Error in opening the file")


class Operations(ReadWrite):
    #find unique words in the list
    def find_unique(self,content):
        unique_words=set(content.split())
        return list(unique_words)

    #count words starting from 'to' and ending with 'ing'
    def countWords(self,cont):
        content=cont.split()
        count=0
        count1=0
        for word in content:
            if word.startswith('to'):
                count=count+1
            if word.endswith('ing'):
                count1=count1+1
        return count,count1

    #return most repeated word in the file
    def repeated_words(self,original):
         return collections.Counter(original.split()).most_common(1)

    #to check if the content in the file consists of any palindrome
    def palindrome(self,uni):
        l=[]
        for word in uni:
            rev = ''.join(reversed(word))
            if word == rev:
                l.append(word)
        return str(l)

    #to return unique list
    def unique_list(self,content):
        return list(content)

    #to convert each word in the file to dictionary with indexing
    def word_dict(self,content):
        return dict(enumerate(content.split(),1))

    #to display the output
    def display(self,ans):
        logging.info(ans)

    #write content in the file whenever necessary
    def write(self,file,content):
        file.write(content)

    # split the words based on vowels
    def split_vowels(self,content):
        return (re.sub(r"(\w)([a,e,i,o,u,A,E,I,O,U])", r"\1 \2", content))

    # capitalise 3rd letter of each word
    def capitalise(self,content):
        read_content = content.split()
        str = ''
        for word in read_content:
            temp = word
            if len(word) > 3:
                temp = word[:2] + word[2].upper() + word[3:]
            if len(word) == 3:
                temp = word[:2] + word[2].upper()
            str = str + ' ' + temp
        return str

    # replace whitespaces with -
    def replace_whitespace(self,content):
        read_content = content.split()
        str = ''
        for word in read_content:
            str = str + word + '-'
        return str

    # use semi colon for new line
    def replace_semicolon(self,content):
        read_content = content.split('.')
        str = ''
        for line in read_content:
            str = str + line + ';\n'
        return str


rf = con.file["readfile"]
obj = Operations(rf)
wf = con.file["writefile"]

file2 = obj.readFile()
logging.info("File opened")
obj.readFile()
logging.info("Number of words starting from 'to' and ending with 'ing' : ")
obj.display(obj.countWords(file2))
logging.info("Word repeated maximum number of times : ")
obj.display(obj.repeated_words(file2))
logging.info("Palindrome present in the file : ")
obj.display(obj.palindrome(file2))
logging.info("Unique list : ")
obj.display(obj.unique_list(obj.find_unique(file2)))
logging.info("Word dictinary : ")
obj.display(obj.word_dict(file2))
file1=obj.writeFile(wf)
logging.info("Write a file : ")
logging.info(obj.write(file1,file2))
logging.info("Split based on vowels : ")
logging.info(obj.write(file1,obj.split_vowels(file2)))
logging.info("Capitalise third letter in each word : ")
logging.info(obj.write(file1,obj.capitalise(file2)))
logging.info("Replace whitespaces with - : ")
logging.info(obj.write(file1,obj.replace_whitespace(file2)))
logging.info("Insert semi colon at end of each line : ")
logging.info(obj.write(file1,obj.replace_semicolon(file2)))
