import unittest
from selenium.webdriver.common.by import By
from src.Main.utils.DriverSetup import browser
from src.Main.TestSteps import AuthModuleSteps
from src.Main.TestData.secret_keys import SecretKeys as SKEYS


class AuthTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    chrome_driver = browser()
    cls.driver = chrome_driver.get_driver()
    cls.steps = AuthModuleSteps.authModule(cls.driver)
    cls.driver.get('https://awork.ge/user/home')

    #close the popup, when page gets loaded
    cls.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()
    cls.steps.open_auth_module()

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

  """
  decision table based test case to test authentication
  TF - Login(true), password(false)
  FT - Login(false), password(true)
  FF - Login(false), password(false)
  TT - Login(true), password(true)
  """


  def test_1_auth_TF(self):
    self.steps.send_credentials(login = SKEYS.login, password = SKEYS.invalid_password)
    result = self.steps.click_authorize()
    self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text)  
    
  def test_2_auth_FT(self):
    self.steps.send_credentials(login = SKEYS.invalid_login, password = SKEYS.Password)
    result = self.steps.click_authorize()
    self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text)  
    
  def test_3_auth_FF(self):
    self.steps.send_credentials(login = SKEYS.invalid_login, password = SKEYS.invalid_password)
    result = self.steps.click_authorize()
    self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text) 

  def test_4_auth_TT(self):
    self.steps.send_credentials(login = SKEYS.login, password = SKEYS.Password)
    result = self.steps.click_authorize()
    self.assertIn('ავტორიზაცია წარმატებულია', result.text)


if __name__ == '__main__':
  unittest.main()