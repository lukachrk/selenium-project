import unittest
from src.Main.TestData.Data_ProfilePage import ProfileData as PFData
from src.Main.TestData.Data_General import generaldata as GLData
from src.Main.PageObject.Locators.Locators_ProfilePage import *

from src.testcases.TestSetup.TestDescription import description
from src.testcases.TestSetup.ProfileSetup import *
import time



class Profile_Update_Module_test(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.PROFILE_UPDATE)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description("entering letter seperated by space in profile update surname field")
  @unittest.skip('validation not implemented yet')
  def test_1_surname_field_validation_for_numbers(self):
    field = Module_locators.SURNAME
    data = GLData.numbers

    steps.fill_out_field(field, data)
    is_invalid_format = steps.field_has_validation(warning_type = GLData.invalid_format)
  
    self.assertTrue(is_invalid_format)

  @description("entering numbers in profile update surname field")
  @unittest.skip('validation not implemented yet')
  def test_2_surname_field_validation_for_spaced_letters(self):
    field = Module_locators.SURNAME
    data = GLData.spaced_letters

    steps.fill_out_field(field, data)
    is_invalid_format = steps.field_has_validation(warning_type = GLData.invalid_format)
  
    self.assertTrue(is_invalid_format)





class Experience_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.WORK_EXPERIENCE)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()


  @description("entering numbers as name in experience module position field")
  @unittest.skip('validation not implemented yet')
  def test_1_position_field_validation_for_numbers(self):
    field = Module_locators.POSITION
    data = GLData.spaced_letters

    steps.fill_out_field(field, data)
    is_invalid_format = steps.field_has_validation(warning_type = GLData.invalid_format)
  
    self.assertTrue(is_invalid_format)

  @description('filling out every mandatory field and checking if save button is enabled')
  def test_2_module_mandatory_fields(self):
    pass

  def test_3_select_options_month(self):
    pass
  
  def test_4_select_option_year(self):
    pass


class Education_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.EDUCATION)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_filds_validations_for_invalid_data(self):
    pass

  def test_2_mandatory_fields(self):
    pass

  def test_3_select_options_year(self):
    pass

  def test_module_for_valid_data(self):
    pass


class Project_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.PROJECTS)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_project_url_validation(self):
    pass

  def test_2_project_url_validation(self):
    pass

class Certificates_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.CERTIFICATES)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

class Skills_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.SKILLS)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()


class ContactInfo_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.EDUCATION)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

class CV_Upload_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(ProfileLocators.MY_CV)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

if __name__ == '__main__':
  unittest.main()


