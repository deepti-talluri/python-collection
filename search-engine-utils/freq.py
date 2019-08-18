import sys

filename = sys.argv[1]
fp = open(filename)
data = fp.read()
words = data.split()
fp.close()
wordfreq = {}
for i in words:
	if i not in wordfreq:
		wordfreq[i] = 0
	wordfreq[i]+= 1
print(wordfreq)
