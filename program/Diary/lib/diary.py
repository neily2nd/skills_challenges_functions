# File: lib/diary.py

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)
        
    
    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        """return an int summed of all the diary using a for loop and using DiaryEntry.count_words"""
        
        return sum(i.count_words()for i in self.entries)
        
        

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
        best_reading_time = time  # Initialize to a large value

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
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.this_chunk = 0
        
        pass

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        words = len(self.contents.split())
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
        words = self.contents.split()
        
        starting_point = self.this_chunk
        ending_point = min(starting_point + time, len(words))
        
        
        chunk = words[starting_point : ending_point]
        self.this_chunk = ending_point
        
        
        
        return " ".join(chunk)


