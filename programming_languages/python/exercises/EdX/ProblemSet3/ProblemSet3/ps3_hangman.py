# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # Create a list of characters from the seceret word
    # Work through all letters guessed, one at a time. Try to look up
    # each guessed character. If this fails, an exception is thrown, breaking
    # the loop. We catch the exeption (which must be "Value Error"), and then
    # continue through the for-loop with 'pass' (not the same thing as "continue"
    # pass is a null operation, required to keep going.

    # We copy the wordCharList from the secret word, and pop out entries which
    # are matched. If all entires are matched, then we have a list with zero
    # length, and we have won the game, else, we have not.
    wordCharList = list(secretWord.lower())
    for letter in lettersGuessed: 
        letterIndex = -1
        try:
            while 1: 
                letterIndex = wordCharList.index(letter,letterIndex+1)
                wordCharList.pop(letterIndex)
        except ValueError:  
            pass
    if len(wordCharList) == 0:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    wordCharList = list(secretWord.lower())

    # Make an empty char list of the same size as the secret word
    # reuse code from above function to fill with guesses, instead of
    # popping out characters
    blanks = []
    for char in wordCharList:
        blanks.append("_")
    for letter in lettersGuessed: 
        letterIndex = -1
        try:
            while 1: 
                letterIndex = wordCharList.index(letter,letterIndex+1)
                blanks[letterIndex] = wordCharList[letterIndex]
        except ValueError:  
            pass
    # concatinate character list into a string
    return ("".join(blanks))
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    # Again, we have to compare one list of characters to another, disregarding
    # order. Additionally, since we are not adding duplicate letters to the
    # list, we only have to compare the letters guessed list to the alphabet.

    # we'll pop letters out of this list which are already guessed.
    alphabetList = list(string.ascii_lowercase)
    
    for letter in lettersGuessed: 
        letterIndex = -1
        try:
            while 1: 
                letterIndex = alphabetList.index(letter,letterIndex+1)
                alphabetList.pop(letterIndex)
        except ValueError:  
            pass
    return ("".join(alphabetList))

def hangman(secretWord):
    lettersGuessed = []
    alphabetList = getAvailableLetters(lettersGuessed)
    preGuessAlpha = 0
    preGuessWord = ""
    postGuessAlpha = 0
    postGuessWord = ""
    guessLeft = 8
    print "Welcome to the game, Hangman!"
    print ("I am thinking of a word that is " + str(len(secretWord)) +" letters long.")
    while guessLeft > 0:

        preGuessAlpha = len(alphabetList)
        preGuessWord = getGuessedWord(secretWord, lettersGuessed)
        
        print "-----------"
        print "You have",guessLeft,"guesses left."
        print "Available Letters:",getAvailableLetters(lettersGuessed)
        inputGuess = raw_input("Please guess a letter: ")
        letterGuessed = inputGuess.lower()
        lettersGuessed.append(letterGuessed[0]) # keep only first letter
        alphabetList = getAvailableLetters(lettersGuessed)

        postGuessAlpha = len(alphabetList)
        postGuessWord = getGuessedWord(secretWord, lettersGuessed)
        
        # Guess is duplicate, or wrong, because we didn't discover new letters.
        if (preGuessWord == postGuessWord):
            # Guess is duplicate, because alphabet remaining didn't shrink
            if preGuessAlpha == postGuessAlpha:
                print "Oops! You've already guessed that letter:",preGuessWord
            else:
                print "Oops! That letter is not in my word:",preGuessWord
                guessLeft-=1
                if guessLeft == 0:
                    print "-----------"
                    print "Sorry, you ran out of guesses. The word was",secretWord
        else:
            print "Good guess:",postGuessWord
            if isWordGuessed(secretWord,lettersGuessed) == True:
                print "-----------"
                print "Congratulations, you won!"
                break
            
## Main Program ##

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)

#lettersGuessed = list(secretWord)
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's'] 
#print "Guessing:"
#print lettersGuessed
#print str(isWordGuessed(secretWord, lettersGuessed))
#print getGuessedWord(secretWord, lettersGuessed)
#print "Available Letters:"
#print getAvailableLetters(lettersGuessed)
