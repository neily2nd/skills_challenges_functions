# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```

```

```python
class TODO():

    def __init__(self):
        self.todo_list = []

    def list_of_tasks(self, task):
        #Parameters:
        #task: (str)a text, tasks
        self.todo_list.append(task)

    def extract_tasks(self):
        #Returns a list of strings representing tasks
        return self.todo_list

    def complete_tasks(self, completed):
        #Parameters:
        #Remove completed tasks from list
        self.todo_list.remove(completed)

# File: lib/diary.py

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry, phone_number=None):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        entry = DiaryEntry(entry, phone_number)
        self.entries.append(entry)


    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

"""    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.


        return sum(i.count_words()for i in self.entries)"""

    def get_phone_numbers(self):
        #Return:
        # An integer "phone number" taken from all diary entries
        return [entry.phone_number for entry in self.entries if entry.phone_number is not None]


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.

        return sum(i.reading_time(wpm) for i in self.entries)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        time = wpm * minutes
        best_entry = None
        best_reading_time = time

        for entry in self.entries:
            reading_time = entry.reading_time(wpm)
            if reading_time <= time and reading_time < best_reading_time:
                best_entry = entry
                best_reading_time = reading_time

        print("Available Time:", minutes, "minutes")
        print("Best Entry:", best_entry)
        print("Reading Time of Best Entry:", best_reading_time)

        return best_entry








# File: lib/diary_entry.py

import math
class DiaryEntry:
    def __init__(self, entry, phone_number):
        # Parameters:
        #   title: string
        #   contents: string
        self.entry = entry
        self.phone_number = phone_number
        self.this_chunk = 0

        pass

"""    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry

        return len(self.contents.split())"""

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        words = len(self.entry.split())
        time_per_word = 1 / wpm
        estimated_time = words * time_per_word
        print(math.ceil(estimated_time))
        return math.ceil(estimated_time)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        time = wpm * minutes
        words = self.entry.split()

        starting_point = self.this_chunk
        ending_point = min(starting_point + time, len(words))


        chunk = words[starting_point : ending_point]
        self.this_chunk = ending_point



        return " ".join(chunk)


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
from lib.diary import *

def test_diary_add():
    test_diary = Diary()
    entry = DiaryEntry("entry to the diary", "01234567891")
    test_diary.add(entry)


    #testing diary.add and diary.all:
    assert test_diary.entries[0].entry == "entry to the diary"
    assert test_diary.entries[0].phone_number == "01234567891"
    assert test_diary.all() == [entry]

    #testing diary.count_words and DiaryEntry.count_words:
    assert test_diary.count_words() == 1

    #testing diary.reading_time and DiaryEntry.reading_time:
    assert test_diary.entries[0].reading_time(50) == 1
    assert test_diary.reading_time(50) == 1



    #testing diary.find_best_entry_for_reading_time:
def test_find_best():
    test_diary = Diary()
    entry1 = DiaryEntry("first entry", "9876543210")  # Takes len("Short contents") words to read
    entry2 = DiaryEntry("second entry pretty long, "456789123456")  # Takes len("Medium contents that require more time") words to read
    entry3 = DiaryEntry("third entry even longer than last", "654987465123")  # Takes len("Long contents that require even more time") words to read
    test_diary.add(entry1)
    test_diary.add(entry2)
    test_diary.add(entry3)

    assert test_diary.find_best_entry_for_reading_time(10, 1) == entry1  # Reading speed: 1 wpm, Available time: 1 minute
    assert test_diary.find_best_entry_for_reading_time(10, 2) == entry1  # Reading speed: 1 wpm, Available time: 2 minutes
    assert test_diary.find_best_entry_for_reading_time(10, 3) == entry1  # Reading speed: 1 wpm, Available time: 3 minutes
    assert test_diary.find_best_entry_for_reading_time(10, 4) == entry1  # Reading speed: 1 wpm, Available time: 4 minutes
    assert test_diary.find_best_entry_for_reading_time(10, 5) == entry1  # Reading speed: 1 wpm, Available time: 5 minutes



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

from lib.todo import *

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


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
