#NLTK Chapter 1 Exercises
#20 Sept 2023
from nltk.book import *

#1
print(12/(4+1))

#2 Given an alphabet of 26 letters, there are 26 to the power of 10. How many
#hundred letter strings are possible?
print(26 ** 100)

#3 Lists
print(['Monty', 'Python'] * 20)
print(3 * sent1)

#4 How many words are there in text2? How many distinct words?
print(len(text2))
print(len(set(text2)))

#5 Compare the lexical diverity scores for humor and romance fiction.
#Which genre is more lexically diverse?
print(len(set(text3)) / len(text3))

def lexical_diversity(text):
    return len(set(text)) / len(text)

print(lexical_diversity(text3))

#6 Produce a dispersion plot of the four main protagonists in sense and sensability
#What can you observe about the differeny roles played by the males and females
#in this movel? can you identify the couples?

text4.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

#7 Find the collocations in text5
#Collocations; sequence of words that occur together unusually often
text5.collocations()

#8 Consider len(set(text4)). State the purpose
len(set(text4))     #how to find the # of unique instances in body of text
len(text4)          # the number of tokens in a given text from start to finish
set(text4)          # all the vocab of a text, the set of tokens w/ no duplicates

#9a
str4 = "I love Sofa"
str4
print(str4)

#9b
str4 + str4
str4 * 2

#10 Define a variable my_sent to be a list of words
#a convert into a string using .join()
#b use split() to split the string back into the list form you had to start
my_sent = ["Sofa", "is", "love"]
print(' '.join(my_sent))
print(my_sent.split())

#11 Define several variable and join them together in various combinations
#what is the relationship between len(phrase1 + phrase2)
#and len(phrase1) + len(phrase2)
phrase1 = ["i", "miss", "my", "dog", "so", "much"]
phrase2 = ["love", "you", "sofa!"]

print(len(phrase1 + phrase2))
print(len(phrase1) + len(phrase2))

#12 Consdier the following experssions, which one will typicaly be more relevant in NLP?
"Monty Python"[6:12]
["Monty", "Python"][1]

# the second would be more relevant because you are manipulating lists
#rather than strings, which can store more data

#13 What does sent1[2][2] do? Why?
print(sent1)
print(sent1[2][2])
print(sent1[0])
print(sent1[2][0:4])

#14 The first sentence of text3 is provided to you in the variable sent3.
#The index of the in sent3 is 1, because sent3[1] gives us 'the'.
#What are the indexes of the two other occurrences of this word in sent3?
print(sent3)
print(sent3[1])
print(sent3[5])
print(sent3[8])

#15 Review conditionals. Find all words in the Chat Corpus (text5)
#starting with the letter b. Show in alphabetical order
print(sorted(w for w in set(text5) if w.startswith('b') and w.isalpha()))

#16 Type the expression list(range(10)) and try:

print(list(range(10)))
print(list(range(10,20)))
print(list(range(10,20,2)))
print(list(range(20, 10, -2)))

#17 Use text9.index() to find the index of the word sunset. By trial and error
#find the slice for the complete sentences that contains this word

text9.index('sunset')
#index 629, lets find the entire sentence
print(text9[621:644])

#18 Using list addition, and set and sorted operations, compute the vocab
#of the sentences sent1 - sent8
sents = sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8
print(sorted(set(w for w in sents if w.isalpha())))

#19 What is the difference between the following lines? Which one is larger?
sorted(set(w.lower() for w in text1))
sorted(w.lower() for w in set(text1))

#the second returns a larger set value because it contains duplicates
#the first returns only a condensed set of tokens found

#20 What is the difference between the following tests:
# w.isupper() = uppercase letters, or changes them to be
# not w.islower() = words that are uppercase, excludes words that start with lowercase

#21 What the slice expressions that extracts the last two words of text2
print(text2[-2:])

#22 Find al the four letter words in the Chat Corpus (text5) With the help
# of a frequency distribution (Freq Dist), show them in decreasing order of freq
freqDist5 = FreqDist(text5)
fourLetterWords = sorted(set([w for w in text5 if w.isAlpha() and len(w) == 4]))

print(fourLetterWords)
print(freqDist5)

for x in [w for w in freqDist5]:
    if x not in fourLetterWords:
        freqDist5.pop()

print(freqDist5)
freqDist5.plot(50)

#23 Use a combo of for and if statements to loop over the words of text6
# and print all the uppercase words, one per line
for word in text6:
    if word.isupper():
        print(word)

#24 Write expressions for finding all words in text6 that meet conditions below
#The result should be in the form of a list of words
# a Ending in 'ise'
sorted([w for w in set(text6) if w.endswith('ise')])
# b containing the letter 'z'
sorted([w for w in set(text6) if 'z' in w])
# c containing the sequence of letters 'pt'
sorted([c for c in set(text6) if 'pt' in c])
# d having all lowercase letters except for an initial capital (titlecase)
sorted([word for word in text6 if word.istitle()])

#25 Define sent to be the list of words
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

# a Print all words beginning with 'sh'
print([s for s in sent if 'sh' in s])
# b Print all words longer than four characters
print([s for s in sent if len(s) > 4])

#26  What does the following code do / how to use it
# to find avg word length of the text
sumofwords = sum(len(w) for w in text1)
#counts the length of each word in text1 and adds all together
print(sumofwords/len(text1))
#avg word length in text1

#27 Define a function called vocab size that hat returns vocab size of text
def vocab_size(text):
    return len(set(text))
print(vocab_size(text4))

#28 Define a function percent(word, text) that calculates how often
#a given word occurs in a text, expressing result as a percentage
def percent(word,text):
    return FreqDist(text)[word]/float(len(text))*100

percent("love", text4)


