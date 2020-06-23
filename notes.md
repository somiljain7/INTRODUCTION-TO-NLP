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


When you want to match a list of terms, it's easier and more efficient to use PhraseMatcher

In natural language processing, a one-hot vector is a 1 × N matrix (vector) used to distinguish each word in a vocabulary from every other word in the vocabulary. 


Np_utils-
is used to convert array of labeled data(from 0 to nb_classes-1) to one-hot vector.



By setting verbose 0, 1 or 2 you just say how do you want to 'see' the training progress for each epoch.
verbose=0 will show you nothing (silent)
verbose=1 will show you an animated progress bar

One Hot encoding of labels.

A one-hot vector is a vector which is 0 in most dimensions, and 1 in a single dimension. In this case, the nth digit will be represented as a vector which is 1 in the nth dimension.


Feature Standardization

It is important preprocessing step. It is used to centre the data around zero mean and unit variance.

##########
from nltk.corpus imports stopwords
text = """The cat is in box. The cat likes box."""
tokens = [ w for w in word_tokenize(text.lower()) if w.isalpha()]
no_stops = [t for t in tokens if t not in stopwords.words('english')]
Counter(no_stops).mostcommon(2)
#output : ('cats',2) ,(box,2)
##########
