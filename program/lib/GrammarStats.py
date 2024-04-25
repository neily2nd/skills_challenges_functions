class GrammarStats:
    def __init__(self):
        self.total_passes = 0
        self.total_checks = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text[0].isupper:
            if text[-1] in "!.,?":
                self.total_checks += 1
                self.total_passes += 1
                return True
        self.total_checks +=1
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return (self.total_passes / self.total_checks) * 100
        
