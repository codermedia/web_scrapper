from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uopen

req = uopen("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")

loaded_data = req.read()

req.close()

html_content = soup(loaded_data,"html.parser")

filename = "flipkart_scrap.csv"
headers = "Brand,Rating,Price,Discount\n"

container = html_content.findAll("div",{"class":"_2kHMtA"})

with open(filename,"w") as f :
    f.write(headers)

    for data in container :
        brand_name = data.findAll("div",{"class":"_4rR01T"})
        rating = data.findAll("div",{"class":"_3LWZlK"})
        price = data.findAll("div",{"class":"_30jeq3 _1_WHN1"})
        discount = data.findAll("div",{"class":"_3Ay6Sb"})

        print(brand_name[0].getText())
        print(rating[0].getText())
        print(price[0].getText())
        print(discount[0].getText())

        f.write(brand_name[0].getText().replace(",","") + "," +rating[0].getText() + "," +price[0].getText()[1:].replace(",","") + "," +discount[0].getText() +"\n")