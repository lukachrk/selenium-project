from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest


class titleSearch(unittest.TestCase):

  def setUp(self):
    self.driver_path = Service("C:/Users/luka/Documents/chromedriver.exe")
    self.driver = webdriver.Chrome(service=self.driver_path)
    self.driver.get('https://awork.ge/user/home')

  def test_title(self):
    assert 'Awork' in self.driver.title

  def tearDown(self):
    self.driver.quit()

if __name__== '__main__':
  unittest.main()