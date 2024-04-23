import pytest
from lib.grammar import *

def test_grammar():
    sentence = grammar("hi this is a sentence")
    
    assert sentence == "Hi this is a sentence."