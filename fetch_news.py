import requests

def fetch_news_article(api_key, query="technology"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            return articles[0]['content']  # Return the content of the first article
        else:
            return "No articles found for the given query."
    else:
        return f"Failed to fetch articles, status code: {response.status_code}"

# Example usage:
api_key = '5339bd783ef549979ee03c05c4933246'
article_text = fetch_news_article(api_key, query="technology")
print(article_text)
