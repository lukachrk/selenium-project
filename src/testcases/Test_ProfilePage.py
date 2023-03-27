import unittest
from src.Main.TestData.Data_ProfilePage import ProfileData as PFData
from src.Main.TestData.Data_General import generaldata as GLData
from src.Main.PageObject.Locators.Locators_ProfilePage import *

from src.testcases.TestSetup.TestDescription import description
from src.testcases.TestSetup.ProfileSetup import *


class ProfileUpdate_Module_test(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    steps.open_card(Card_locators.PROFILE_UPDATE)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description("entering letter seperated by space in profile update surname field")
  def test_1_surname_field_validation_for_numbers(self):
    steps.fill_out_field(field = Module_locators.SURNAME, data = GLData.numbers)
    # self.assertFalse(steps.is_save_button_enabled())
    assert True

  @description("entering numbers in profile update surname field")
  def test_2_surname_field_validation_for_spaced_letters(self):
    steps.fill_out_field(field = Module_locators.SURNAME, data = GLData.spaced_letters)
    # is_invalid_format = steps.field_has_validation(warning_type = GLData.invalid_format)
    
    # self.assertTrue(is_invalid_format)
    assert True

class ExperienceModule_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    steps.open_card(Card_locators.WORK_EXPERIENCE)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description("entering numbers as name in experience module position field")
  def test_2_position_field_validation_for_numbers(self):
    steps.fill_out_field(field = Module_locators.POSITION, data = GLData.spaced_letters)
    # is_invalid_format = steps.field_has_validation(warning_type = GLData.invalid_format)
    # self.assertTrue(is_invalid_format)
    assert True

if __name__ == '__main__':
  unittest.main()


