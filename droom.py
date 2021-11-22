from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

url = "https://droom.in/cars"
driver = webdriver.Chrome(
    'D:\Myproject\python\webscrap\chromedriver\chromedriver.exe')
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find_all(
    'div', {'class': 'jss210 card-body'})

links = []
for div in all_divs:
    aa = div.find('a', href=True)
    links.append(aa['href'])

driver.close()
count = 1
for link in links:
    count += 1
    driver = webdriver.Chrome(
        'D:\Myproject\python\webscrap\chromedriver\chromedriver.exe')
    driver.get(link)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find('div', {
                    'class': 'd-position-relative d-padding-20 d-padding-top-15 d-padding-bottom-0 listing-card'})
    print(div.text)
    driver.close()
