from nltk.book import *

###22
##freqDist5 = FreqDist(text5)
##commonDesc = []
##
##for x in freqDist5:
##    if len(x) == 4 and x.isalpha():
##        commonDesc.append(x)
##
##print(commonDesc)

freqDist5 = FreqDist(text5)
fourlw = sorted(set([w for w in freqDist5 if w.isalpha() and len(w)==4]))

for x in [w for w in freqDist5]:
    if x not in fourlw:
        freqDist5.pop(x)

print(freqDist5)
freqDist5.plot(50)








