import pytest
from lib.count_words import *


def test_count_words_type():
    with pytest.raises(Exception) as e:
        count_words(123)
    error = str(e.value)
    assert error == "Not a string"
    
def test_count_words():
    count = count_words("hello this is five words")
    assert count == 5