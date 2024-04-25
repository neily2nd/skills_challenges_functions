from lib.DiaryEntry import *

def test_init():
    diary_entry = DiaryEntry("test1", "test2")
    result = diary_entry.format()
    assert result == "test1: test2"
        
        
def test_count_words():
    diary_entry = DiaryEntry("test1", "test2")
    result = diary_entry.format()
    count_result = diary_entry.count_words()
    assert count_result == 2
    
def test_reading_time():
    diary_entry = DiaryEntry("test1", "test2")
    reading_time = diary_entry.reading_time(50)
    assert reading_time == 1
    
    
#Given I don't know what to write in these things but being inspired by a better developer
#reading_chunk returns a chunk of the contents
#based on wpm and minutes

def test_reading_chunk():
    diary_entry = DiaryEntry("test1", "test2 and some more words for testing this")
    reading_time = diary_entry.reading_chunk(2, 2)
    assert reading_time == "test2 and some more"
    
def test_chunk_again():
    diary_entry = DiaryEntry("test1", "test2 and some more words for testing this")
    assert diary_entry.reading_chunk(2,2) == "test2 and some more"
    assert diary_entry.reading_chunk(2,2) == "words for testing this"
    