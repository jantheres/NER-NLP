import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download necessary NLTK models
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_entities_nltk(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    entities = ne_chunk(tagged)
    return entities

# Example usage:
example_text = "Barack Obama was the 44th President of the United States."
nltk_entities = extract_entities_nltk(example_text)
for entity in nltk_entities:
    if hasattr(entity, 'label'):
        print(entity)
