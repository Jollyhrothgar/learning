# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
import string
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if len(aStr) == 0:
        return aStr
    else:
        first = aStr[:-1]
        return aStr[-1]+reverseString(first)
#
# Problem 4: Erician
#


def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO
    # We get true iff every x is in word, and the order is correct
    if len(x) == 0:
        return True
    if word == "":
        return False
    elif x[0] in word:
        if len(x) == 1:
            return True
        if len(word) > 1:
            index = word.find(x[0])+1
            return True and x_ian(x[1:len(x)],word[index:len(word)])
        elif len(word) == 1:
            return True
    else:
        return False

   

#
# Problem 5: Typewriter
#
import string
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    words = string.split(text," ")
    print words
