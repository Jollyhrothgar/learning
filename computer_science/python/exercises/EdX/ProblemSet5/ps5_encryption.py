# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random
import re

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    # The structure of the dict associates each letter to its cipher counterpart
    # We populate two lists, one with uppercase letters, another with lowercase letters
    # and then build a dict using the cipher shift.
    # We need to use an index and shifted index to access the appropriate letters in each list
    # and then we can terminate our shifting once the dict has reached the right size.
    # The encoder actually self-organizes (and in any case, in a dict, the hash is what matters,
    # rather than the order. The only important aspect is associating the right cipher to letter.
    
    index = 0
    if shift > 25: 
        shift = shift%26
    shiftedIndex = index + shift
    alphaLower = list(string.ascii_lowercase)
    alphaUpper = list(string.ascii_uppercase)

    encoder = {} # Merge Lower And Uppercase when both are filled.
    while index < 26:
        if shiftedIndex > 25:
            shiftedIndex -= 26
        encoder[alphaLower[index]] = alphaLower[shiftedIndex]
        encoder[alphaUpper[index]] = alphaUpper[shiftedIndex]
        index += 1
        shiftedIndex = index + shift
    return encoder

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    
    result = ""
    for char in text:
        if char in coder:
            result+=coder[char]
        else:
            result+=char
    return result


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text,buildCoder(shift))
    
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    wordsFound = 0
    bestShift = 0
    for shiftGuess in range(26):
        wordsFoundCurrent = 0
        shiftGuessString = applyShift(text,(26-shiftGuess)%26)
        words = shiftGuessString.split(" ")
        for word in words:
            if isWord(wordList,word):
                wordsFoundCurrent+=1
        if wordsFoundCurrent > wordsFound:
            bestShift = shiftGuess    
            wordsFound = wordsFoundCurrent
    if(26-bestShift == 26):
        return 0
    else:
        return 26-bestShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    myStory = getStoryString()
    loadWords()
    return applyShift(myStory,findBestShift(wordList,myStory))

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    decryptStory()
