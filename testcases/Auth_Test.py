import unittest
from testcases.DriverSetup import browser
from selenium.webdriver.common.by import By

class AuthTest(unittest.TestCase):

  def setUp(self):
    #change the path to your driver directory
    self.browser = browser(path='C:/Users/luka/Documents/chromedriver.exe')
    self.driver = self.browser.get_driver()
    self.driver.get('https://awork.ge/user/home')

    #close the popup, when page loaded
    self.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()

  """
  TF - Login(true), password(false)
  FT - Login(false), password(true)
  FF - Login(false), password(false)
  TT - Login(true), password(true)
  """


  def test_auth_TF(self):
    authmodule = page.authModule(self.driver)
    authmodule.open_auth_module()

    authmodule.send_credentials(login = '123', password = '123')
    result = authmodule.click_authorize()
    self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text)  
    
  # def test_auth_FT(self):
  #   authmodule = page.authModule(self.driver)
  #   authmodule.open_auth_module()

  #   authmodule.send_credentials(login = '123', password = '123')
  #   result = authmodule.click_authorize()
  #   self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text)  
    
  # def test_auth_FF(self):
  #   authmodule = page.authModule(self.driver)
  #   authmodule.open_auth_module()

  #   authmodule.send_credentials(login = '123', password = '123')
  #   result = authmodule.click_authorize()
  #   self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text) 

  # def test_auth_TT(self):
  #   authmodule = page.authModule(self.driver)
  #   authmodule.open_auth_module()

  #   authmodule.send_credentials(login = '123', password = '123')
  #   result = authmodule.click_authorize()
  #   self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text)


  # def test_vacancy_filter(self):
  #   Vacancy = page.MainPage(self.driver)
  #   result = Vacancy.search_vacancy(text='mdzgoli')
  #   self.assertTrue('შედეგი არ მოიძებნა' in result.text)

  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
  unittest.main()