import requests 
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-18&sortBy=publishedAt&apiKey=ce6efb02a1ba4afebeea4e29bef1a20a"
print(url)
api = "ce6efb02a1ba4afebeea4e29bef1a20a"
r = requests.get(url)
data = r.json()
articles = data["articles"]
for article in articles:
    print(article['title'])
    print(article['url'])
    print("---")