import string
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
        #print (str(alphaLower[index])+", "+str(alphaLower[shiftedIndex]))
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
    ### TODO

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
    return applyCoder(text,buildCoder(shift))
