from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ser = Service("C:/Users/luka/Documents/chromedriver.exe")
op = Options()

op.add_argument('--ignore-certificate-errors')
op.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service=ser,options=op)

driver.get('https://awork.ge/user/home')
driver.close()