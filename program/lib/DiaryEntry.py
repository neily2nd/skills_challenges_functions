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
        

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        
        self.formatted_diary =  f"{self.title}: {self.contents}"
        return self.formatted_diary
        

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        if not self.formatted_diary:
            self.format()
        self.counted_words = len(self.formatted_diary.split())
        print(f"this is the counted words: {self.counted_words}")
        return self.counted_words

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        self.wpm = wpm
        self.estimated_time = len(self.contents.split()) / self.wpm
        return math.ceil(self.estimated_time)
        
        

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
        ending_point = self.this_chunk + time
        
        
        chunk = words[starting_point : ending_point]
        self.this_chunk = min(ending_point, len(words))
        
        #if this_chunk >= len(self.contents)
            
        return " ".join(chunk)
            
        
