# Scrape laptop details from singerSL product_id,price,description,url...?
# use BeautifulSoup for parser
# use request for http

from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

for i in range(4):
    #open pages one by one
    url_to_scrape = "https://www.singersl.com/electronics/laptops?filter=&sort_by=field_weight&sort_order=DESC&page=" #0,1,2,3 

    # get pages using request
    request_page = urlopen(url_to_scrape)
    page_html = request_page.read()
    request_page.close()

    # get html parser

    html_soup = BeautifulSoup(page_html,'html.parser')

    # get laptop sections
    laptops = html_soup.find_all('div',class_="product-item")
    #print(laptops)
    
    # first open a csv file to write (first time only)
    if(i==0):
        filename = 'singerLaptops.csv'
        f = open(filename,'w')
        # add headers to csv file
        headers = 'Product_id,Price,description,url\n'
    
    for laptop in laptops:
        # find details
        product_id = laptop.find('div',class_="sku").text
        price = laptop.find('div',class_="selling-price").text
        price = price.replace(',','')
        toUrl = laptop.find('div',class_="content")
        toUrl = toUrl.find_next('a')
        url = format(toUrl.get("href"))
        url = "https://www.singersl.com"+url
        description = laptop.find('div',class_="content")
        description = description.find_next('a').text
        # description is not clear need processing
        description = description.replace(",","")

        #write to csv
        f.write(product_id+','+price+','+description+','+url+',\n')


        if(i==4):  #close the file finally
            f.close()

#done
# description should be processed later