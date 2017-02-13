'''Webscraper for Austin Computers website to get graphics card name and price'''

from bs4 import BeautifulSoup
import requests

websiteURL = "http://www.umart.com.au/newsite/category.php?id=610&pagesize=3"
productNum = 0

link = requests.get(websiteURL)
soup = BeautifulSoup(link.content, "lxml")
productsList = soup.find('ul', class_="list_pic")
for productFind in productsList.find_all('li', class_='item'):
    productNum += 1
    product = productFind.find_next('div', class_='goods-name')
    productName = product.find_next('a')
    productPrice = productName.find_next('em', class_="sale-price") 
    print repr(productNum).rjust(2), productName.get_text(), productPrice.get_text()
    
