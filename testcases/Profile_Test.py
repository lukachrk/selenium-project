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
    authmodule = page.authModule(self.driver)
    authmodule.open_auth_module()

    #provide your credentials here to authorize into system
    authmodule.send_credentials(login = '', password = '')
    authmodule.click_authorize()

  def test_navigation(self):
    pass

  def test_about_section(self):
    pass

  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
  unittest.main()