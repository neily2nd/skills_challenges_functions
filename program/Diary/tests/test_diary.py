from lib.diary import *

def test_diary_add():
    test_diary = Diary()
    entry = DiaryEntry("titlehere", "contentshere")
    test_diary.add(entry)
    
    
    #testing diary.add and diary.all:
    assert test_diary.entries[0].title == "titlehere"
    assert test_diary.entries[0].contents == "contentshere"
    assert test_diary.all() == [entry]
    
    #testing diary.count_words and DiaryEntry.count_words:
    assert test_diary.count_words() == 1
    
    #testing diary.reading_time and DiaryEntry.reading_time:
    assert test_diary.entries[0].reading_time(50) == 1
    assert test_diary.reading_time(50) == 1
    


    #testing diary.find_best_entry_for_reading_time:
def test_find_best():
    test_diary = Diary()
    entry1 = DiaryEntry("Title 1", "Short contents")  # Takes len("Short contents") words to read
    entry2 = DiaryEntry("Title 2", "Medium contents that require more time")  # Takes len("Medium contents that require more time") words to read
    entry3 = DiaryEntry("Title 3", "Long contents that require even more time")  # Takes len("Long contents that require even more time") words to read
    test_diary.add(entry1)
    test_diary.add(entry2)
    test_diary.add(entry3)
    
    assert test_diary.find_best_entry_for_reading_time(10, 1) == entry1  # Reading speed: 1 wpm, Available time: 1 minute
    assert test_diary.find_best_entry_for_reading_time(10, 2) == entry1  # Reading speed: 1 wpm, Available time: 2 minutes
    assert test_diary.find_best_entry_for_reading_time(10, 3) == entry1  # Reading speed: 1 wpm, Available time: 3 minutes
    assert test_diary.find_best_entry_for_reading_time(10, 4) == entry1  # Reading speed: 1 wpm, Available time: 4 minutes
    assert test_diary.find_best_entry_for_reading_time(10, 5) == entry1  # Reading speed: 1 wpm, Available time: 5 minutes
