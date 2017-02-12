'''Webscraper for Netplus Micro Computers website to get graphics card name and price'''

from bs4 import BeautifulSoup
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

websiteURL = "http://www.netplus.com.au/product-list/VD999/Graphics_Card/"
productNum = 0
pagenum=1

#Function to find relevant html tags and texts
def scrapePage(websiteURL):
    "Function takes in a URL and scrapes it"
    r = requests.get(websiteURL)
    soup = BeautifulSoup(r.content, "lxml")
    findProducts = soup.find('div', class_="productlistcontainer")
    for productList in findProducts.find_all('table', class_="productlist"):
        for product in productList.find_all('td', class_='img'):
            global productNum
            productSort = product.find_next('b')
            productName = productSort.get_text()
            productNum = productNum + 1
            productPrice = productSort.find_next('td')
            price = productPrice.find_next('td')
            print productNum, productName, price.get_text()

scrapePage(websiteURL)

    


