from lib.diary_todo import *

def test_diary_add():
    test_diary = Diary()
    entry = DiaryEntry("entry to the diary", "01234567891")
    test_diary.add(entry)


    #testing diary.add and diary.all:
    assert test_diary.entries[0].entry == "entry to the diary"
    assert test_diary.entries[0].phone_number == "01234567891"
    assert test_diary.all() == [entry]

    

    #testing diary.reading_time and DiaryEntry.reading_time:
    assert test_diary.entries[0].reading_time(50) == 1
    assert test_diary.reading_time(50) == 1



    #testing diary.find_best_entry_for_reading_time:
def test_find_best():
    test_diary = Diary()
    entry1 = DiaryEntry("first entry", "9876543210")
    entry2 = DiaryEntry("second entry pretty long", "456789123456")
    entry3 = DiaryEntry("third entry even longer than last", "654987465123")
    test_diary.add(entry1)
    test_diary.add(entry2)
    test_diary.add(entry3)

    assert test_diary.find_best_entry_for_reading_time(10, 1) == entry1  
    assert test_diary.find_best_entry_for_reading_time(10, 2) == entry1  
    assert test_diary.find_best_entry_for_reading_time(10, 3) == entry1  
    assert test_diary.find_best_entry_for_reading_time(10, 4) == entry1  
    assert test_diary.find_best_entry_for_reading_time(10, 5) == entry1
    
    
    
    ############Unit Testing############################
    
def test_empty_task():
    todo = TODO()
    assert todo.extract_tasks() == []

def test_list():
    todo = TODO()
    todo.list_of_tasks("vacuum")
    assert todo.extract_tasks() == ["vacuum"]

def test_complete():
    todo = TODO()
    todo.list_of_tasks("vacuum")
    todo.list_of_tasks("wash up")
    todo.complete_tasks("wash up")
    assert todo.extract_tasks() == ["vacuum"]