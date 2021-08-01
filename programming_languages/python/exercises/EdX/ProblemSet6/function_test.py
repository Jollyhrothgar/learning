import string
def clearPunctuation(text):
    if len(text) == 0:
        return text
    elif text[0] in string.punctuation:
        return " "+clearPunctuation(text[1:len(text)])
    else:
        return text[0]+clearPunctuation(text[1:len(text)])
