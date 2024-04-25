from lib.GrammarStats import *

#Given a string
#return true if string has Capitalize and last char is in "!.,?"

def test_check():
    checking = GrammarStats()
    assert checking.check("Hello this is a sentence.") == True
    
def test_percentage_good():
    checking = GrammarStats()
    assert checking.check("hi this is not valid") == False
    assert checking.check("Hello this is a sentence.") == True
    assert checking.percentage_good() == 50

