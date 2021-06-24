"""     Testing    """
import collections
import logging
import re
import configfile as con

#pylint: disable=no-self-use
logging.basicConfig(filename='file.log', level=logging.INFO,
                    format='%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')


#pylint: disable=useless-object-inheritance
class ReadWrite(object):
    """ Read and Write file location """

    filename = 'abc.txt'
    # pylint: disable=inconsistent-return-statements
    def read_content_file(self):
        """ Read file location """
        with open(self.filename, 'r') as file:
            read_content = file.read()
            return read_content

    def write_file_content(self, write_file):
        """ Write file location """
        file = open(write_file, 'w')   #pylint: disable=consider-using-with
        return file


class Operations(ReadWrite):
    """Perform operations"""
    def find_unique(self):
        """find unique words in the list"""
        unique_words = set(self.read_content_file().split())
        return list(unique_words)

    def count_words(self):
        """ count words starting from 'to' and ending with 'ing' """
        content = self.read_content_file().split()
        count = 0
        count1 = 0
        for word in content:
            if word.startswith('to'):
                count = count+1
            if word.endswith('ing'):
                count1 = count1+1
        return count, count1

    def repeated_words(self):
        """ return most repeated word in the file """
        return collections.Counter(self.read_content_file().split()).most_common(1)

    def palindrome(self):
        """to check if the content in the file consists of any palindrome"""
        list_pal = []
        for word in self.find_unique():
            rev = ''.join(reversed(word))
            if word == rev:
                list_pal.append(word)
        return str(list_pal)

    def unique_list(self):
        """to return unique list"""
        return list(self.find_unique())

    def word_dict(self):
        """to convert each word in the file to dictionary with indexing"""
        return dict(enumerate(self.read_content_file().split(), 1))

    def display(self, ans):
        """to display the output"""
        logging.info(ans)

    def write(self, file, content):
        """write content in the file whenever necessary"""
        file.write(content)

    def split_vowels(self):
        """split the words based on vowels"""
        return re.sub(r"(\w)([a,e,i,o,u,A,E,I,O,U])", r"\1 \2", self.read_content_file())

    def capitalise(self):
        """capitalise 3rd letter of each word"""
        read_content = self.read_content_file().split()
        str1 = ''
        for word in read_content:
            temp = word
            if len(word) > 3:
                temp = word[:2] + word[2].upper() + word[3:]
            str1 = str1 + ' ' + temp
        return str1

    def replace_whitespace(self):
        """replace whitespaces with -"""
        read_content = self.read_content_file().split()
        str1 = ''
        for word in read_content:
            str1 = str1 + word + '-'
        return str1

    def replace_semicolon(self):
        """use semi colon for new line"""
        read_content = self.read_content_file().split('.')
        str1 = ''
        for line in read_content:
            str1 = str1 + line + ';\n'
        return str1


#RF = con.file["readfile"]
WF = con.file["writefile"]
obj = Operations()

file2 = obj.read_content_file()
logging.info("File opened")
obj.read_content_file()

logging.info("Number of words starting from 'to' and ending with 'ing' : ")
obj.display(obj.count_words())

logging.info("Word repeated maximum number of times : ")
obj.display(obj.repeated_words())

logging.info("Palindrome present in the file : ")
obj.display(obj.palindrome())

logging.info("Unique list : ")
obj.display(obj.unique_list())

logging.info("Word dictinary : ")
obj.display(obj.word_dict())

file1 = obj.write_file_content(WF)
logging.info("Write a file : ")
logging.info(obj.write(file1, file2))

logging.info("Split based on vowels : ")
logging.info(obj.write(file1, obj.split_vowels()))

logging.info("Capitalise third letter in each word : ")
logging.info(obj.write(file1, obj.capitalise()))

logging.info("Replace whitespaces with - : ")
logging.info(obj.write(file1, obj.replace_whitespace()))

logging.info("Insert semi colon at end of each line : ")
logging.info(obj.write(file1, obj.replace_semicolon()))
