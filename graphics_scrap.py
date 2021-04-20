import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req 

#get web page and parse and store
my_url = "https://www.newegg.com/p/pl?d=graphics+card"
client_page = req(my_url)
page_html = client_page.read()
client_page.close
page_soup = soup(page_html,"html.parser")


#reading the web page contents
graphics = page_soup.find_all('div',class_='item-container')

#check how many graphics card found
len(graphics)

# go through all the graphics card and save info to csv file and print to Screen
filename = "products.csv"
file = open(filename, "w")
header = "Title, Price in $, Shipping Details\n"
file.write(header)
for graphic in graphics:
    title = graphic.find('a',class_="item-title").text
    price = re.findall(r"\$\d+(?:\.\d+)?", graphic.find('li',class_="price-current").text)
    shipping = graphic.find('li',class_="price-ship").text
    
    print("Title: " + title)
    print("Price: " + price[0])
    print("Shipping: "+ shipping)
    
    file.write(title.replace(",","|") +","+ price[0] + "," + shipping.strip() + "\n")
file.close()
