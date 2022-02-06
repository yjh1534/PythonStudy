from bs4 import BeautifulSoup
import requests

#Get Page from URL
response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

#create Soup
soup = BeautifulSoup(web_page, "html.parser")

#attrs of 1st article
first_article = soup.find(name="a", class_="titlelink")
first_title = first_article.getText()
first_link = first_article["href"]
first_upvote = soup.find(name="span", class_= "score").getText()

print(first_title)
print(first_link)
print(first_upvote)

#attrs about every articles
article_titles = []
article_links = []
articles = soup.find_all(name="a", class_="titlelink")
for article in articles:
    article_titles.append(article.getText())
    article_links.append(article["href"])
upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_= "score")]

#Find most voted article
max_index = upvotes.index(max(upvotes))

print(article_titles[max_index])
print(article_links[max_index])
print(upvotes[max_index])


