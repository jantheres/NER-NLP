import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_entities_spacy(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Example usage:
example_text = "Barack Obama was the 44th President of the United States."
spacy_entities = extract_entities_spacy(example_text)
print(spacy_entities)
