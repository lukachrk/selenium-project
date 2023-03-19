import unittest
from testcases.DriverSetup import browser
from PageObject import page
from selenium.webdriver.common.by import By
from collections import namedtuple

class Profile_test(unittest.TestCase):

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
    self.driver.get("https://awork.ge/user/profile")



  # def test_navigation(self):
  #   navigation = page.Profile(self.driver)

  #   navigation.navigate_to(navlink='პროფილი')
  #   self.assertIn('nav=profile', self.driver.current_url) 

  #   navigation.navigate_to(navlink='გაგზავნილი აპლიკაციები')
  #   self.assertIn('nav=sent', self.driver.current_url)    

  #   navigation.navigate_to(navlink='შენახული ვაკანსიები')
  #   self.assertIn('nav=saved', self.driver.current_url)    

  #   navigation.navigate_to(navlink='სამუშაოს შეტყობინებები')
  #   self.assertIn('nav=job_alerts', self.driver.current_url)    

  #   navigation.navigate_to(navlink='პარამეტრები')
  #   self.assertIn('nav=settings', self.driver.current_url)

  
  def test_about_module(self):
    modules = page.Profile(self.driver)

    fields = namedtuple('fields', ['name','surname','profession'])
    modules.open_module('ჩემს შესახებ')

    fields_data = fields('luka','luka','tester')
    modules.fill_out(module='about_module', data=fields_data)

  # def test_b_section(self):
  #   modules = page.Profile(self.driver)
  #   modules.open_module('პროექტები')

  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
  unittest.main()