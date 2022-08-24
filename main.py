import bs4 
import requests

response = requests.get("htt[s://news.ycombinator.com/news")

yc_webpage = response.text

soup = bs4.BeautifulSoup(yc_webpage , "html.parser")


article = soup.find(name = "a" , class_="storylink")
article_text = article.getText()
article_link = article.get("href")
article_upvote = soup.find(name="span",class_="score").getText()


 










 