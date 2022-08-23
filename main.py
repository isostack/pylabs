import bs4 
import lxml 

with open("website.html" , encoding="utf8") as file:
    contents = file.read()

soup = bs4.BeautifulSoup(contents , "html.parser")

print(soup.title.text)