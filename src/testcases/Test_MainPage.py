import unittest
from src.Main.TestSteps import Steps_MainPage
from src.Main.utils.DriverSetup import browser
from selenium.webdriver.common.by import By
from src.testcases.TestSetup.TestDescription import description


class AuthTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    chrome_driver = browser()
    cls.driver = chrome_driver.get_driver()
    cls.steps = Steps_MainPage.MainPage(cls.driver)
    cls.driver.get('https://awork.ge/user/home')

    #close the popup, when page gets loaded
    cls.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


  #test whetever we get error messeage or not for searching for a vacancy that can't be found
  def test_vacancy_filter(self):
    result = self.steps.search_vacancy(text='abc123')
    self.assertTrue('შედეგი არ მოიძებნა' in result.text)


if __name__ == '__main__':
  unittest.main()