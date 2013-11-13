from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
import nltk.classify.util
from write_tak import write_tak

def word_feats(words):
    return dict([(word, True) for word in words])
 
def sentiment_analysis(text, output_file=None):
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
 
    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4
 
    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
    classifier = NaiveBayesClassifier.train(trainfeats)

    feats = word_feats(word_tokenize(text))
    sentiment = classifier.classify(feats)
    write_tak(sentiment, output_file)
    return sentiment