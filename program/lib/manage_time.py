#managing time task

"""take an amount of time, give the amount of words and calculate they are under a specific value"""

def time(minutes, words):
    word_per_minute = words / 200
    if word_per_minute > minutes:
        return f"You cannot complete this reading"