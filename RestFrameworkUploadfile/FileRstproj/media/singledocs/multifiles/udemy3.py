import requests
from bs4 import BeautifulSoup

url="https://www.udemy.com/topic/python/free/"



res=requests.get(url).content

soup=BeautifulSoup(res,'html.parser')
# print(soup.prettify())

title=soup.find("div",class_="udlite-focus-visible-target udlite-heading-md course-card--course-title--2f7tE")
print(title)

author=soup.find("div",class_="udlite-text-xs course-card--instructor-list--lIA4f")
print(author)

rating=soup.find("span",class_="star-rating--star-wrapper--2eczq")
print(rating)

price=soup.find("div",class_="price-text--price-part--Tu6MH course-card--discount-price--3TaBk udlite-heading-md")
print(price)
