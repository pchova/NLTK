from __future__ import division
from nltk.corpus import genesis

def lexical_diversity(some_data):
    word_count = len(some_data)
    vocab_size = len(set(some_data))
    diversity_score = vocab_size / word_count
    return diversity_score

kjv = genesis.words('english-kjv.txt')
print(lexical_diversity(kjv))

##same as the function below
##def lexical_diversity(text):
##        return len(text) / len(set(text))

