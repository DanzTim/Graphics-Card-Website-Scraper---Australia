'''Web scraper for Australia MSY website which scrapes graphics cards name and price'''

#Only works for MSY online webstore with valid location inside the URL. for example: waonline, viconline etc.
import requests
from bs4 import BeautifulSoup

pagenum = 1
websiteURL = "http://www.msy.com.au/waonline/14-graphics-card"#You can change the location /waonline/ to /viconline/ etc. in the URL.
productNum = 0

#Function to scrape page based on the given URL above.
def scrapePage(websiteURL):
    "Function takes in a URL and scrapes it"
    r = requests.get(websiteURL)
    soup = BeautifulSoup(r.content, "lxml")
    listview = soup.find('div', id="list-view")
    for productName in listview.find_all('a', { "class" : "product_img_link" }):
        global productNum;
        productNum = productNum + 1
        productPrice = productName.find_next("span", class_="price" )
        print productNum, productName.get('title'), productPrice.get_text()
    return

#Scrapes all the 11 pages for the graphics card section of the MSY website    
while pagenum != 12:
    if pagenum == 1:#Page one does not need extended URL
        scrapePage(websiteURL)
    else:           #Page 2 and above needs extended URL: /page-2 etc.
        websiteURL = websiteURL+"/page-"+str(pagenum)
        scrapePage(websiteURL)
    pagenum+=1



    


