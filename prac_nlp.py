import spacy
#from sklearn.linear_model import LogisticRegression
nlp=spacy.load('en_core_web_md')
text="the quick brown fox,jump over the hill"
doc=nlp(text)
for token in doc:
    print(token.text)