import unittest
from testcases.DriverSetup import browser
from PageObject import page
from selenium.webdriver.common.by import By

class AuthTest(unittest.TestCase):

  def setUp(self):
    #change the path to your driver directory
    self.browser = browser(path='C:/Users/luka/Documents/chromedriver.exe')
    self.driver = self.browser.get_driver()
    self.driver.get('https://awork.ge/user/home')

    #close the popup, when page gets loaded
    self.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()

  #search for a vacancy that couldn't be in the db
  def test_vacancy_filter(self):
    Vacancy = page.MainPage(self.driver)
    result = Vacancy.search_vacancy(text='mdzgoli')
    self.assertTrue('შედეგი არ მოიძებნა' in result.text)

  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
  unittest.main()