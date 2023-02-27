from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest
import page


class browser:
  service, options = None, None

  def __init__(self):
    self.path = "C:/Users/luka/Documents/chromedriver.exe"
    self.service = Service(self.path)
    self.options = Options()
    # self.options.add_argument('--headless')


  def get_driver(self):
    return webdriver.Chrome(service=self.service,options=self.options)



class titleSearch(unittest.TestCase):

  def setUp(self):
    self.browser = browser()
    self.driver = self.browser.get_driver()
    self.driver.get('https://awork.ge/user/home')
    self.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()

  def test_vacancy_filter(self):
    Vacancy = page.MainPage(self.driver)
    Vacancy.send_input = "abc"
    assert Vacancy.search_start()

  def tearDown(self):
    self.driver.quit()

if __name__== '__main__':
  unittest.main()