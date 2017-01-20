'''Web scraper for Australia PLE website which scrapes graphics cards name and price'''

import requests
from bs4 import BeautifulSoup

websiteURL = "https://www.ple.com.au/Categories/Graphics-Cards"#Change website URL to anything inside the PLE website store 

link = requests.get(websiteURL)
soup = BeautifulSoup(link.content, "lxml")

productNum = 0
for product in soup.find_all('span', { "class" : "vc_productdesc" }):
    productNum += 1
    productName = product.find('a')
    productPrice = product.find_next('div', class_='vc_productrowprice')
    getPrice = productPrice.find('span', class_='vc_productprice')
    print productNum, productName.get_text(), getPrice.get_text()
    



    


