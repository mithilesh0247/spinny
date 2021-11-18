from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

url = "https://www.spinny.com/used-maruti-suzuki-cars-in-delhi-ncr/s/"
driver = webdriver.Chrome(
    'D:\Myproject\python\webscrap\chromedriver\chromedriver.exe')
driver.get(url)
time.sleep(15)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find_all(
    'div', {'class': 'CarListingDesktop__carListingCarWrapper'})


header = ['name', 'km', 'fuel', 'type', 'price']

with open('spinnyData.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    for div in all_divs:
        data = []
        model = div.find(
            'div', {'class': 'styles__yearAndMakeAndModelSection'}).text
        km = div.find('p', {'class': 'styles__otherInfoSection'}).text
        price = div.find('div', {'class': 'styles__priceSection'}).text
        data.append(model)
        if km[8] == 'p':
            if km[len(km) - 1] == 'c':
                data.append(km.replace('petrolautomatic', ''))
            else:
                data.append(km.replace('petrolmanual', ''))
            data.append('petrol')
        else:
            if km[len(km) - 1] == 'c':
                data.append(km.replace('dieselautomatic', ''))
            else:
                data.append(km.replace('dieselmanual', ''))
            data.append('diesel')
        if km[len(km) - 1] == 'c':
            data.append('automatic')
        else:
            data.append('manual')
        data.append(price.replace('‚¹', ''))
        writer.writerow(data)


driver.close()
