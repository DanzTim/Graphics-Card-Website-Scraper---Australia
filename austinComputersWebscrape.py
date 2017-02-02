'''Webscraper for Austin Computers website to get graphics card name and price'''

from bs4 import BeautifulSoup
import requests

websiteURL = "http://www.austin.net.au/shop-categories/video-graphics-cards.html"
productNum = 0
pagenum=1

#Function to scrape page based on the given URL above.
def scrapePage(websiteURL):
    "Function takes in a URL and scrapes it"
    r = requests.get(websiteURL)
    soup = BeautifulSoup(r.content, "lxml")
    for findProducts in soup.find_all('li', class_="item"):
        productName = findProducts.find('a')
        global productNum;
        productNum = productNum + 1
        productPrice = findProducts.find_next('span', class_="regular-price")
        name = productName.find_next('a').get_text("|", strip=True)
        #Using str.split() to get rid of everything after "- " for the name. If you want to include it, just remove .split("- ")[0]
        print repr(productNum).rjust(2), name.split("- ")[0], productPrice.get_text()
    return

#Scrapes all the 5 pages for the graphics card section of the Austin Computers website    
while pagenum <= 5:
    if pagenum == 1:#Page one does not need extended URL
        scrapePage(websiteURL)
    else:           #Page 2 and above needs extended URL using ?p=2.
        websiteURL = websiteURL+"?p="+str(pagenum)
        scrapePage(websiteURL)
    pagenum+=1



    


