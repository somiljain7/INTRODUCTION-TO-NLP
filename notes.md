spaCy is the leading library for NLP, and it has quickly become one of the most popular Python frameworks. 
spaCy relies on models that are language-specific and come in different sizes. You can load a spaCy model with spacy.load.

preprocessing
lemmatizing (lemma of a word is its base form)
like cool from cooling

stopwords are words that occur frequently in the language and dont contain much information( the, is, ans but not)


token.lemma_ returns lemma 

token.is_stop(true if stopword else false)

Pattern matching 
matching tokens or phrases within chunks of text or whole documents
