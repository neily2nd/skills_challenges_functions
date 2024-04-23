def count_words(word):
    #checking word is a string
    if type(word) != str:
        raise Exception("Not a string")
    #return the length of word when split
    
    return len(word.split())   
    
        