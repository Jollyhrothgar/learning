import nltk
import random
from nltk.corpus import movie_reviews

# Create training and testing sets
documents = [(list(movie_reviews.words(fileid)),category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# end up doing:
# Take every word in every review
# Take list of words, find most popular words
# of those popular words, which appear in positive reviews
# which appears more in negative reviews

# compile words
all_words = []
for w in movie_reviews.words():
    w = w.lower()
    all_words.append(w.lower())

# use features of documents (words) to figure out positive or negative reviews.

# NLTK frequency distribution
all_words = nltk.FreqDist(all_words)
#print all_words.most_common(15)

# how often does stupid pop up?
#print all_words["stupid"]

word_features = list(all_words.keys())[:3000]

# document is the first part of the tuple in documents. So, we get all the words
# in the set.
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words) # creates a boolean, if word is in top 3000
    return features

# negative reviews - looking up which of the top 3000 words appear in some
# negative reviews.
print find_features(movie_reviews.words('neg/cv000_29416.txt'))

# rev = review
# category = pos or neg
featuresets = [(find_features(rev),category) for (rev,category) in documents]

training_set = featuresets[:1900] 
testing_set = featuresets[1900:]

## Naieve Bayes Classifier
# posterior (likelihood) = prior occurences * likligood / evidence 
# (do for positive, do for negative)

## Create classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)
print "Naive Bayes Algo % accuracy:",(nltk.classify.accuracy(classifier,training_set))*100.
classifier.show_most_informative_features(15)


