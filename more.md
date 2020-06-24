# TF-IDF FORMULA
TFIDF WEIGHT  FOR TOKEN i IN DOCUMENT j  =   NO. OF OCCURENCE OF TOKEN i IN DOC j *LOG(  TOTAL NUMBER OF DOCUMENTS / NO. OF DOCS THAT CONTAIN i)

# weight will be low if the term doesnt appear often in the document because the tf variable will then be low
# weight will also be low if log is close to 0 means internal equation is low

# words that occurs many or all docs will have a very low tf-idf weight
