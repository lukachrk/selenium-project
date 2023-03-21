import unittest
from src.Main.utils.DriverSetup import browser
from src.Main.TestSteps import AuthModuleSteps, ProfilePageSteps
from selenium.webdriver.common.by import By
from src.Main.TestData.ProfilePageData import ProfileData as PFD
from src.Main.TestData.secret_keys import SecretKeys as SKEYS

class Profile_test(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    chrome_driver = browser()
    cls.driver = chrome_driver.get_driver()
    cls.steps = ProfilePageSteps.Profile(cls.driver)
    cls.driver.get('https://awork.ge/user/home')

    #close the popup, when page gets loaded
    cls.driver.find_element(By.CLASS_NAME, 'btn.btn-medium').click()
    authmodule = AuthModuleSteps.authModule(cls.driver)
    authmodule.open_auth_module()

    #provide your credentials here to authorize into system
    authmodule.send_credentials(login = SKEYS.login, password = SKEYS.Password)

    authmodule.click_authorize()
    cls.driver.get("https://awork.ge/user/profile")

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

  def test_1_navigation_urls(self):
    self.steps.navigate_to(navlink = 'პროფილი')
    self.assertIn('nav=profile', self.driver.current_url) 

    self.steps.navigate_to(navlink = 'გაგზავნილი აპლიკაციები')
    self.assertIn('nav=sent', self.driver.current_url)    

    self.steps.navigate_to(navlink = 'შენახული ვაკანსიები')
    self.assertIn('nav=saved', self.driver.current_url)    

    self.steps.navigate_to(navlink = 'სამუშაოს შეტყობინებები')
    self.assertIn('nav=job_alerts', self.driver.current_url)    

    self.steps.navigate_to(navlink = 'პარამეტრები')
    self.assertIn('nav=settings', self.driver.current_url)

  
  def test_2_about_module_inputs_validation(self):
    self.steps.navigate_to('პროფილი')
    self.steps.open_module('ჩემს შესახებ')
    input_data = (PFD.name, PFD.surname, PFD.profession)

    self.steps.fill_out(module='about_module', data=input_data)
    assert self.steps.is_button_enabled()


if __name__ == '__main__':
  unittest.main()