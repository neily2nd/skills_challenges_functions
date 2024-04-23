def make_snippet(word):
    
    if type(word) != str:
        raise Exception("Not a string")
    elif len(word) >= 6:
        snipped_word = word[0:5] + "..."
        return snipped_word
    else:
        return word
            
        
    