#chapter 2 Exercises NLTK 10/11/23
import nltk

#1. Create a variable phrase containing a list of words.
#Review the operations described in the previous chapter,
#including addition, multiplication, indexing, slicing, and sorting

##phrase = ['My', 'friends', 'are', 'good', 'people']
##
##phrase.insert(1,5)
##print(phrase)
##
##print(phrase*3)
##
##phrase.pop(4)
##print(phrase)
##
##phrase.insert(5,'love')
##print(phrase)
##
##print(phrase[:5])   #prints from beginning to 5
##print(phrase[3:])   #prints from 3 to end of list
##print(phrase[:])    #beginning to the end of list


#2 Use the corpus module to explore austen-persuasion.txt
#How many word tokens does this book have? How many word types?
#(within gutenberg corpus)


##from nltk.corpus import gutenberg
##print(gutenberg.fileids())
##print(len(gutenberg.words('austen-persuasion.txt')))
##print()
##persuasion = gutenberg.words('austen-persuasion.txt')
##print(len(persuasion))
##print(len(set(w.lower() for w in persuasion)))


#3 Use brown corpus reader or web text corpus to access
#some sample text in two different genres
#nltk.corpus.brown.words()
#nltk.corpus.webtext.words()

##from nltk.corpus import webtext
##print(webtext.fileids())
##
##for fileid in webtext.fileids():
##    print(fileid, webtext.words(fileid)[:20], '...')
##    
##from nltk.corpus import brown
##print('\nCategories')
##print(brown.categories())
##
##print(brown.words(categories='mystery')[:20])
##print(brown.sents(categories=['adventure', 'hobbies', 'religion']))


#4 Read in the texts of the State of the Union addres using state_union
#  corpus reader. Count occurance of men, women, and people in each doc
#  What has happened to the usage of words over time?

##from nltk.corpus import state_union
##
##cfd = nltk.ConditionalFreqDist(
##        (fileid, word)
##        for fileid in state_union.fileids()
##        for word in state_union.words(fileid))
##
##personList = ['women', 'men', 'people']
##fileidss = state_union.fileids()
##
##cfd.tabulate(conditions=fileidss, samples=personList)

##women = 0
##men = 0
##people = 0
##
##for fileid in state_union.fileids():
##    for w in state_union.words(fileid):
##        if w.lower().startswith('women'):
##            women += 1
##        elif w.lower().startswith('men'):
##            men += 1
##        elif w.lower().startswith('people'):
##            people += 1
##
##print("Occurance of Words in the State of the Union Address Over Time\n")
##print("Occurance of women:", women)
##print("Occurance of men:", men)
##print("Occurance of people:", people)
##
##cfd = nltk.ConditionalFreqDist((word, fileid)
##        for fileid in state_union.fileids()
##        for w in state_union.words(fileid)
##        for word in ['women', 'men', 'people']
##        if w.lower().startswith(word))
##cfd.plot()
                

#5 Investigate the holonym-meronym relations for some nouns.
#  3 kinds of relations, so you will need to use
#  member_meroynms(), part_meronyms(), substance_meronyms()
#  member_holonyms(), part_holonyms(), substance_holonyms()
#  meronym = 'components'
#  holonym = 'things they are contained in'

##from nltk.corpus import wordnet as wn
##
##print(wn.synsets('ocean'))
##print(wn.synset('ocean.n.02').lemma_names())
##print(wn.synset('ocean.n.02').definition())
##
##print('\n', wn.synsets('boat'))
##for synset in wn.synsets('boat'):
##    print(synset.lemma_names())
##
##boat = wn.synset('boat.n.01')
##types = boat.hyponyms()
##types[0]
##print(sorted(lemma.name() for synset in types for lemma in synset.lemmas()))
##
##print('Synsets: ', wn.synsets('species'))
##print('\nPart Meronyms:', wn.synset('species.n.01').part_meronyms())
##print('\nSubstance Meronyms:', wn.synset('species.n.01').substance_meronyms())
##print('\nMember Meronyms:', wn.synset('species.n.01').member_meronyms())
##
##print('\nPart Holonyms:', wn.synset('species.n.01').part_holonyms())
##print('\nSubstance Holonyms:', wn.synset('species.n.01').substance_holonyms())
##print('\nMember Holonyms:', wn.synset('species.n.01').member_holonyms())


#6 In the discussion of comparative wordlist, we created an object called
#  translate which you could look up using words in both German and Spanish
#  in order to get corresponding words in English. What problem might arise
#  with this approach?

#the translate object can be used to find basic meanings of words
#but many words have multiple meanings or POS which can affect how its
#translated, as seen with translating dog vs that

##from nltk.corpus import swadesh
##en2es = swadesh.entries(['en', 'es'])
##print(en2es[:10])
##
##translate = dict(en2es)
##print(translate['dog'])
##print(translate['that'])


#7 According to Strunk and White's Elements of Style, the word however,
##used at the start of a sentence, means "in whatever way" or "to whatever
##extent", and not "nevertheless". They give this example of correct usage:
##However you advise him, he will probably do as he thinks best.
##Use the concordance tool to study actual usage of this word in the
##various texts we have been considering. See also the LanguageLog
##posting "Fossilized prejudices about'however'" at
##http://itre.cis.upenn.edu/~myl/languagelog/archives/001913.html

##from nltk.corpus import webtext
##print(webtext.fileids())
##
##text1 = nltk.Text(nltk.corpus.webtext.words('overheard.txt'))
##text1.concordance("however")
##
##from nltk.corpus import brown
##print(brown.categories())
##
##text4 = nltk.Text(nltk.corpus.brown.words(categories='romance'))
##text4.concordance("however")
##
##
##text5 = nltk.Text(nltk.corpus.brown.words(categories=['mystery', 'lore']))
##text5.concordance("however")


#8 Define a conditional frequency distribution over the Names corpus that
## allows you to see which initial letters are more frequent for males
## vs females

##names = nltk.corpus.names
##cfd = nltk.ConditionalFreqDist(
##            (fileid, name[0])
##            for fileid in names.fileids()
##            for name in names.words(fileid))
##cfd.plot()


#9 Pick a pair of texts and study the difference between them, in terms of
## vocab, vocabulary richness, genre, etc. Can you find pairs of words
## which have quite difference meanings across 2 texts, such as
## monstrous in Moby Dick and Sense and Sensability

from nltk.book import *
print("\n", text1)
print(text1.concordance("monstrous"))
print(text1.similar("monstrous"))

print("\n", text2)
print(text2.concordance("monstrous"))
print(text2.similar("monstrous"))
































    































