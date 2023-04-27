from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random

path = Service('chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=path)
df = pd.read_csv("restaurants.csv")

list_price_mean = []
for i in range(9250):
    url = df.href[i]
    driver.get(url)
    sleep(random.randint(5, 6))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all("div", {"class": "current-price"})

    sum = 0

    for link in links:
        sum += int(link.text.replace(',', '').replace('đ', ''))

    if len(links) == 0:
        list_price_mean.append(0)
    else:
        list_price_mean.append(int(sum/len(links)))

print(len(list_price_mean))

df_price = pd.DataFrame(list_price_mean, columns=['price'])

df_price.to_csv("price5.csv", index=False)
