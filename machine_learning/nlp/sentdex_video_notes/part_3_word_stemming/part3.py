"""
Stemming words using the porter-stemmer
"""
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# Exmaple - these two sentence mean exactly the same thing
sentence_1 = "I was taking a ride in the car."
sentence_2 = "I was riding in a car."

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

#for w in example_words:
#    print(ps.stem(w))

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print (ps.stem(w))
