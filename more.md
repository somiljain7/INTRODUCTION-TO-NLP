# TF-IDF FORMULA
TFIDF WEIGHT  FOR TOKEN i IN DOCUMENT j  =   NO. OF OCCURENCE OF TOKEN i IN DOC j *LOG(  TOTAL NUMBER OF DOCUMENTS / NO. OF DOCS THAT CONTAIN i)

# weight will be low if the term doesnt appear often in the document because the tf variable will then be low
# weight will also be low if log is close to 0 means internal equation is low

# words that occurs many or all docs will have a very low tf-idf weight
# example
tf-idf make for more interesting results on the document level

# Create a new TfidfModel using the corpus: tfidf
        tfidf = TfidfModel(corpus)
        
        # Calculate the tfidf weights of doc: tfidf_weights
        tfidf_weights = tfidf[doc]
        
        # Print the first five weights
        print(tfidf_weights[:5])
        
        # Sort the weights from highest to lowest: sorted_tfidf_weights
        sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
        
        # Print the top 5 weighted words
        for term_id, weight in sorted_tfidf_weights[:5]:
            print(dictionary.get(term_id), weight)

    [(24, 0.0022836332291091273), (39, 0.0043409401554717324), (41, 0.008681880310943465), (55, 0.011988285029371418), (56, 0.005482756770026296)]
    reverse 0.4884961428651127
    infringement 0.18674529210288995
    engineering 0.16395041814479536
    interoperability 0.12449686140192663
    reverse-engineered 0.12449686140192663

