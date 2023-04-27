from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random
path = Service('chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=path)
areas_list = ["quan-1", "quan-2", "quan-3", "quan-4", "quan-5",
                 "quan-6", "quan-7", "quan-8", "quan-9", "quan-10",
                 "quan-11", "quan-12", "quan-binh-thanh", "quan-tan-binh",
                 "quan-phu-nhuan", "quan-tan-phu", "quan-go-vap", "quan-binh-tan",
                 "tp-thu-duc", "huyen-binh-chanh", "huyen-nha-be", "huyen-hoc-mon",
                 "huyen-cu-chi", "huyen-can-gio"]
base_url = "https://www.foody.vn/ho-chi-minh/quan-an-tai-{area}?c=quan-an&categorygroup=food"

login_url = "https://id.foody.vn/account/login?returnUrl=https://www.foody.vn/"

driver.get(login_url)
sleep(5)
input_email = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/form/fieldset/div[2]/div/input")
input_email.send_keys("Phuoctran1818@gmail.com")

input_pass = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/form/fieldset/div[3]/div/input")
input_pass.send_keys("Phuoc123456")

login_button = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[3]/form/fieldset/input")
login_button.click()
sleep(10)


for i in range(1):

    url = base_url.format(area=areas_list[23])

    driver.get(url)
    sleep(10)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    num_Items = soup.find('span', {'data-bind': True})
    num_Items = int(num_Items.text.replace(',',''))

    nloop = int((num_Items/5)/12)
    for j in range(2):

        load_all_link = driver.find_element(By.XPATH, "/html/body/div[2]/section/div/div[2]/div/div/div/div/div[2]/div[8]/a")
        load_all_link.click()

        sleep(random.randint(2, 3))
    print("oke")
    sleep(5)
    print("oke")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all('a', {'data-bind': True}, target="_blank")

    list_links = []
    # Lặp qua tất cả các liên kết
    for link in links:
        # Lấy giá trị của thuộc tính 'href' và 'title'
        href = link.get('href')
        if (href is not None) and ("https" in href):
            list_links.append(href)

df = pd.DataFrame(list_links, columns=['href'])

df.to_csv('data_huyenCanGio.csv', index=False)

driver.quit()
