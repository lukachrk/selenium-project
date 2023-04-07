from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class browser:
  def __init__(self, path ='src/Main/utils/chromedriver.exe'):
    self.path = path
    self.service = Service(self.path)
    self.options = Options()
    self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.options.add_argument('--headless')


  def get_driver(self):
    return webdriver.Chrome(service=self.service,options=self.options)