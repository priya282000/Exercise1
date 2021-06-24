import pytest
from ex import *

class TestOperations():
    def test_count_words(self):
        test1 = Operations().count_words()
        test2 = (1, 1)
        assert test1 == test2

    def test_repeated_words(self):
        test1 = Operations().repeated_words()
        test2 = [('am', 3)]
        assert test1 == test2

    def test_palindrome(self):
        test1 = Operations().palindrome()
        test2 = "['I']"
        assert test1 == test2

    def test_word_dict(self):
        test1 = Operations().word_dict()
        test2 = {1: 'I', 2: 'am', 3: 'Padma', 4: 'Priya.I', 5: 'am', 6: 'from', 7: 'Coimbatore.I', 8: 'am', 9: 'doing', 10: 'intern', 11: 'at', 12: 'adf.I', 13: 'like', 14: 'to', 15: 'listen', 16: 'music', 17: 'malayalam.'}
        assert test1 == test2

    def test_split_words(self):
        test1 = Operations().split_vowels()
        test2 = 'I am P adm a Pr iy a.I am fr om C oimb at or e.I am d oing int ern at adf.I l ik e t o l ist en m us ic m al ay al am.\n'
        assert test1 in test2

    def test_capitalise(self):
        test1 = Operations().capitalise()
        test2 = ' I am PaDma PrIya.I am frOm CoImbatore.I am doIng inTern at adF.I liKe to liSten muSic maLayalam.'
        assert test2 in test1

    def test_replace_whitespace(self):
        test1 = Operations().replace_whitespace()
        test2 = 'I-am-Padma-Priya.I-am-from-Coimbatore.I-am-doing-intern-at-adf.I-like-to-listen-music-malayalam.-'
        assert test2 in test1

