from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import datetime

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# options.add_argument('--crash-dumps-dir=/tmp')
# options.add_argument('--remote-debugging-port=9222')
options.binary_location = "c:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(executable_path=r'c:\\utils\\chromedriver_win32\\chromedriver.exe', options=options)
user_login = "admin"
user_password = "arn58gb4"
driver.get('http://192.168.0.1')
# print(driver.page_source)
# sleep(2)
credentials = driver.find_elements(By.CLASS_NAME, 'input-example')
credentials[0].send_keys(user_login)
credentials[1].send_keys(user_password)
driver.find_element(By.ID, 'start').click()
sleep(5)

while True:
    driver.get('http://192.168.0.1/status-and-support.html#sub=1')
    sleep(2)
    dns1 = driver.find_element(By.ID, 'inter_primary_dns').text
    dns2 = driver.find_element(By.ID, 'inter_secondary_dns').text
    if dns1 != '94.140.14.49' and dns2 != '94.140.14.59':
        driver.get('http://192.168.0.1/settings.html#sub=52')
        sleep(2)
        driver.find_element(By.ID, 'ip6_dhcp_server').click()
        driver.find_element(By.ID, 'ip6_router_advertisement').click()
        driver.find_element(By.ID, 'applyButton').click()
        print("correct DNS in " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sleep(60)
