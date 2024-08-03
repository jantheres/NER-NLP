# Named Entity Recognition (NER) Comparison: NLTK vs spaCy

This project demonstrates the comparison between rule-based Named Entity Recognition (NER) using NLTK and machine learning-based NER using spaCy. The comparison is showcased through a simple web application built with Streamlit.

## Project Overview

The application fetches news articles from the News API and extracts named entities using two different approaches:
- **NLTK**: A rule-based approach using NLTK's built-in methods.
- **spaCy**: A machine learning-based approach using the pre-trained `en_core_web_sm` model from spaCy.

The results from both approaches are displayed and compared within the app, highlighting the strengths and weaknesses of each.

## Features

- Fetches the latest news articles using the News API.
- Extracts named entities using NLTK and spaCy.
- Provides a comparison of the results from both methods.
- User-friendly interface built with Streamlit.

## Requirements

- Python 3.7+
- `requests`
- `nltk`
- `spacy`
- `streamlit`

You can install the required packages using pip:

```bash
pip install requests nltk spacy streamlit


import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

python -m spacy download en_core_web_sm
streamlit run ner_app.py
