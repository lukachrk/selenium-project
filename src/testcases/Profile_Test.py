import unittest
from src.testcases.DriverSetup import browser
from src.Main.TestSteps import AuthModuleSteps, ProfilePageSteps
from collections import namedtuple
from selenium.webdriver.common.by import By

class Profile_test(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    #change the path to your driver directory
    chrome_driver = browser(path='C:/Users/luka/Documents/chromedriver.exe')
    cls.driver = chrome_driver.get_driver()
    cls.driver.get('https://awork.ge/user/home')

    #close the popup, when page gets loaded
    cls.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()
    authmodule = AuthModuleSteps.authModule(cls.driver)
    authmodule.open_auth_module()

    #provide your credentials here to authorize into system
    authmodule.send_credentials(login = '', password = '')

    authmodule.click_authorize()
    cls.driver.get("https://awork.ge/user/profile")

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

  def test_navigation(self):
    navigation = ProfilePageSteps.Profile(self.driver)

    navigation.navigate_to(navlink='პროფილი')
    self.assertIn('nav=profile', self.driver.current_url) 

    navigation.navigate_to(navlink='გაგზავნილი აპლიკაციები')
    self.assertIn('nav=sent', self.driver.current_url)    

    navigation.navigate_to(navlink='შენახული ვაკანსიები')
    self.assertIn('nav=saved', self.driver.current_url)    

    navigation.navigate_to(navlink='სამუშაოს შეტყობინებები')
    self.assertIn('nav=job_alerts', self.driver.current_url)    

    navigation.navigate_to(navlink='პარამეტრები')
    self.assertIn('nav=settings', self.driver.current_url)

  
  def test_modules(self):
    modules = ProfilePageSteps.Profile(self.driver)
    modules.open_module('ჩემს შესახებ')
    input_data = namedtuple('fields', ['name','surname','profession'])

    fields_data = input_data('luka','luka','tester')
    modules.fill_out(module='about_module', data=fields_data)


if __name__ == '__main__':
  unittest.main()