from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize 
word = word_tokenize ("Decentralization is cool")
word_lengths = [ len(w) for w in words]
plt.hist(word_lengths)
plt.show()
