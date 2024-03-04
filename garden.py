import spacy

nlp = spacy.load("en_core_web_sm")
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The man with the telescope saw the ship sink.",
    "The time traveling tourist visited London in 1888."
]
for sentence in gardenpathSentences:
    # Tokenize the sentence (split into words)
    doc = nlp(sentence)

    # Perform named entity recognition (NER)
    for entity in doc.ents:
        print(f"{entity.text} ({entity.label_})")  # Print entity text and label

        # Look up and print explanation for unknown entities
        if entity.label_ not in ("PERSON", "ORG", "GPE", "LOC", "DATE", "CARDINAL", "ORDINAL"):
            print(spacy.explain(entity.label_))
         