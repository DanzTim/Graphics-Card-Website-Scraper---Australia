'''Webscraper for VTechIndustries website to get graphics card name and price'''

from bs4 import BeautifulSoup
import requests

websiteURL = "http://www.vtechindustries.com.au/computer-hardware/video-cards"
productNum = 0
pagenum=1

#Function to scrape page based on the given URL above.
def scrapePage(websiteURL):
    "Function takes in a URL and scrapes it"
    r = requests.get(websiteURL)
    soup = BeautifulSoup(r.content, "lxml")

    productsList = soup.find('ol', class_="products-list")
    for findProducts in productsList.find_all('h2', class_="product-name"):
        productName = findProducts.find('a')
        global productNum;
        productNum = productNum + 1
        productPrice = productName.find_next('span', class_="price")
        print repr(productNum).rjust(2), productName.get('title'), productPrice.get_text()
    return

#Scrapes all the 5 pages for the graphics card section of the VTechIndustries website    
while pagenum <= 5:
    if pagenum == 1:#Page one does not need extended URL
        scrapePage(websiteURL)
    else:           #Page 2 and above needs extended URL using ?p=2.
        websiteURL = websiteURL+"?p="+str(pagenum)
        scrapePage(websiteURL)
    pagenum+=1



    


