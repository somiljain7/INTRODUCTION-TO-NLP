import spacy
nlp = spacy.load('en')
doc = nlp("Tea is healthy and calming, don't you think?")
for token in doc:
    print(token)
