import bs4 

# in order to make connection with the webpage
from urllib.request import urlopen as uReq

# in order to parse html content 
from bs4 import BeautifulSoup as soup  

# store  the required url in a variable .
my_url = "https://www.newegg.com/p/pl?d=graphics&N=100007709&name=Desktop%20Graphics%20Cards"


# make a connection 
uClient = uReq(my_url)

# read the entire web page 
page_html = uClient.read()

# close the connection 
uClient.close()

# parse the reed web page using beautiful soup 
page_soup = soup(page_html,"html.parser")


# get all the individual product details 
containers = page_soup.findAll("div",{"class":"item-container"}) 

# in order to avoid first 3 boxes which of no use.
containers = containers[4:]

# let's store the data inside a csv file 
filename = "graphics.csv"
f      = open(filename,"w")
headers = "product,description,shiping_price,price\n" 

f.write(headers)

# looping through each of the products in order to get product details
for container in containers:
    
    # get the product name
    product = container.find("div",{"class":"item-info"})
    product = product.div.a.img["title"]
    
    # get the product description
    title_container = container.findAll("a",{"class":"item-title"})
    prod_descrip    = title_container[0].text
    
    # get the shipping price value
    ship_price = container.findAll("li",{"class":"price-ship"})
    shiping_price = ship_price[0].text.strip()
    
    
    # get the current price of the product
    price = container.find("li",{"class":"price-current"}).text.strip()
    price = dollor.split()[0]
    
    f.write(product + "," + prod_descrip + "," + shiping_price + "," +  price + "\n")
f.close()    