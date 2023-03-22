import unittest
from selenium.webdriver.common.by import By
from src.Main.utils.DriverSetup import browser
from src.Main.TestSteps import AuthModuleSteps, ProfilePageSteps
from src.Main.TestData.ProfilePageData import ProfileData as PFData
from src.Main.TestData.GeneralData import generaldata as GLData
from src.Main.TestData.secret_keys import SecretKeys as SKEYS
from src.testcases.TestDescription import description

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

  @description("Test profile update module fields validation when entering numbers")
  def test_2_pu_module_fields_validation_for_numbers(self):
    self.steps.navigate_to('პროფილი')
    self.steps.open_module('PROFILE_UPDATE')

    self.steps.fill_out_fields(module='about_module', data=GLData.numbers)
    self.assertFalse(self.steps.is_save_button_enabled())

  @description("Test profile update module fields validation when entering spacings")
  def test_3_pu_module_fields_validation_for_spacings(self):
    self.steps.fill_out_fields(module='about_module', data=GLData.spacings)
    self.assertFalse(self.steps.is_save_button_enabled())

  @description("Test profile update module fields validation when entering letters seperated by space")
  def test_4_pu_module_fields_validation_for_spaced_inputs(self):
    self.steps.fill_out_fields(module='about_module', data=GLData.spaced_letters)
    self.assertFalse(self.steps.is_save_button_enabled())  
    
  @description("Test profile update module fields validation when entering too many characters")
  def test_5_pu_module_fields_validation_for_too_many_chars(self):
    self.steps.fill_out_fields(module='about_module', data=GLData.too_many_chars)
    self.assertFalse(self.steps.is_save_button_enabled())  
    
  @description("Test work experience module, when skipping mandatory field")
  def test_6_wx_module_mandatory_fields_validation(self):
    self.steps.fill_out_fields(module='about_module', data=GLData.too_many_chars)
    self.assertFalse(self.steps.is_save_button_enabled())

  

if __name__ == '__main__':
  unittest.main()