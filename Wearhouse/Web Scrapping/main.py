import bs4 
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = bs4.BeautifulSoup(yc_webpage , "html.parser")

articles = soup.find_all(name = "a" , class_="titlelink")
article_texts = []
article_links = []
for item in articles:
    article_texts.append(item.getText())
    article_links.append(item.get("href"))
       
article_upvotes = [item.get_text() for item in soup.find_all(name="span",class_="score")]

article_upvotes_int = [int(item.split()[0]) for item in article_upvotes]

highest_index = article_upvotes_int.index(max(article_upvotes_int))

print(article_texts[highest_index])
print(article_links[highest_index])
print(article_upvotes_int[highest_index])



 










 