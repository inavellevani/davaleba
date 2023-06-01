import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('biblus.csv','w',newline='',encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['title', 'price'])
num = 1
for i in range(5):
    url = f'https://biblusi.ge/products?category=291&page={num}'
    response = requests.get( url )
    soup = BeautifulSoup( response.text, 'html.parser' )
    dv = soup.find( 'div', {'class': 'row'} )
    titles = [elem.text for elem in dv.find_all( 'div', {'class': 'font-size-1rem font-weight-700 __book-name'} )]
    prices = [elem.text.strip().replace( '\n', '' ).replace( ' ', '' ) for elem in dv.find_all( 'div', {'class': 'text-primary font-weight-700'} )]
    data = zip(titles, prices)
    writer.writerows(data)
    num+=1
    sleep(randint(5,10))