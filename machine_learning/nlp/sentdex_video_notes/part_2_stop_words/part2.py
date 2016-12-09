from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = []
#for word in words:
#    if word not in stop_words:
#        filtered_sentence.append(word)
filtered_sentence = [word for word in words if not word in stop_words]
print filtered_sentence
