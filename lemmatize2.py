 # Import WordNetLemmatizer
        from nltk.stem import WordNetLemmatizer
        
        # Retain alphabetic words: alpha_only
        alpha_only = [t for t in lower_tokens if t.isalpha()]
        
        # Remove all stop words: no_stops
        no_stops = [t for t in alpha_only if t not in english_stops]
        
        # Instantiate the WordNetLemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()
        
        # Lemmatize all tokens into a new list: lemmatized
        lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
        
        # Create the bag-of-words: bow
        bow = Counter(lemmatized)
        
        # Print the 10 most common tokens
        print(bow.most_common(10))
# [('debugging', 40), ('system', 25), ('software', 16), ('bug', 16), ('problem', 15), ('tool', 15), ('computer', 14), ('process', 13), ('term', 13), ('used', 12)]

