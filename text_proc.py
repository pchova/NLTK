from __future__ import division
def lexical_diversity(some_data):
    word_count = len(some_data)
    vocab_size = len(set(some_data))
    diversity_score = vocab_size / word_count
    return diversity_score

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def lexical_diversity2(text):
    return len(text) / len(set(text))

def percentage(count, total):
    return 100 * count / total


