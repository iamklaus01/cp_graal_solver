"""
import stanza

class NERExtractor:
    def __init__(self):
        stanza.download('fr')

    def extract_named_entities(self, text):
        # initialize stanza pipeline
        nlp = stanza.Pipeline('en', processors='tokenize,ner')

        # process the text to extract named entities
        doc = nlp(text)

        # get named entities and their labels
        named_entities = []
        for sent in doc.sentences:
            for ent in sent.ents:
                named_entities.append((ent.text, ent.type))

        return named_entities
"""
