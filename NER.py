import requests
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
import spacy

# Initialize spaCy model
nlp = spacy.load('en_core_web_sm')

# Download necessary NLTK models
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Function to fetch news article
def fetch_news_article(api_key, query="technology"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            return articles[0]['content']  # Return the content of the first article
        else:
            return "No articles found for the given query."
    else:
        return f"Failed to fetch articles, status code: {response.status_code}"

# Function to extract entities using NLTK
def extract_entities_nltk(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    entities = ne_chunk(tagged)
    return entities

# Function to extract entities using spaCy
def extract_entities_spacy(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Fetch news article
api_key = '5339bd783ef549979ee03c05c4933246'
article_text = fetch_news_article(api_key, query="technology")

# Ensure we have some content to process
if article_text and isinstance(article_text, str):
    # Extract entities using NLTK
    nltk_entities = extract_entities_nltk(article_text)
    print("Entities from NLTK:")
    for entity in nltk_entities:
        if hasattr(entity, 'label'):
            print(entity)
    
    # Extract entities using spaCy
    spacy_entities = extract_entities_spacy(article_text)
    print("\nEntities from spaCy:")
    for entity in spacy_entities:
        print(entity)
    
    # Compare the results
    print("\nComparison of NER Results:")
    nltk_entity_list = [" ".join([word for word, pos in tree.leaves()]) for tree in nltk_entities if hasattr(tree, 'label')]
    spacy_entity_list = [entity[0] for entity in spacy_entities]
    
    common_entities = set(nltk_entity_list).intersection(set(spacy_entity_list))
    unique_nltk_entities = set(nltk_entity_list).difference(set(spacy_entity_list))
    unique_spacy_entities = set(spacy_entity_list).difference(set(nltk_entity_list))

    print(f"Common Entities: {common_entities}")
    print(f"Entities unique to NLTK: {unique_nltk_entities}")
    print(f"Entities unique to spaCy: {unique_spacy_entities}")
else:
    print("No valid article content to process.")
