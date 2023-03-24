import unittest
from src.Main.TestData.ProfilePageData import ProfileData as PFData
from src.Main.TestData.GeneralData import generaldata as GLData
from src.testcases.TestDescription import description
from src.testcases.BaseTestSetups.ProfileSetup import *


class ProfileUpdate_Module_test(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    steps.open_module('PROFILE_UPDATE')

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description("entering letter seperated by space in profile update surname field")
  def test_1_surname_field_validation_for_numbers(self):
    steps.fill_out_field(module = 'profile_update', field = 'SURNAME', data = GLData.numbers)
    self.assertFalse(steps.is_save_button_enabled())

  @description("entering numbers in profile update surname field")
  def test_2_surname_field_validation_for_spaced_letters(self):
    steps.fill_out_field(module = 'profile_update', field = 'SURNAME', data = GLData.spaced_letters)
    self.assertFalse(steps.is_save_button_enabled())

class ExperienceModule_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    steps.open_module('WORK_EXPERIENCE')

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description("entering spaced letters in experience module employer field")
  def test_1_employer_field_validation_for_spaced_letters(self):
    steps.fill_out_field(module = 'work_experience', field = 'EMPLOYER', data = GLData.spaced_letters)
    self.assertTrue(steps.is_save_button_enabled())

  @description("entering spaced letters in experience module position field")
  def test_2_position_field_validation_for_many_chars(self):
    steps.fill_out_field(module = 'work_experience', field = 'POSITION', data = GLData.spaced_letters)
    self.assertTrue(steps.is_save_button_enabled())


if __name__ == '__main__':
    unittest.main()
