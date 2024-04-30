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

##########################################################################################

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
        #entry = DiaryEntry(entry, phone_number)
        self.entries.append(entry)


    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries



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








######################################################################################################################

import math
class DiaryEntry:
    def __init__(self, entry, phone_number):
        # Parameters:
        #   title: string
        #   contents: string
        self.entry = entry
        self.phone_number = phone_number
        self.this_chunk = 0
        print("below is entry and phone number")
        print(self.entry)
        print(self.phone_number)

        



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
        print("Below is the estimated time:")
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
    
    
    
    
