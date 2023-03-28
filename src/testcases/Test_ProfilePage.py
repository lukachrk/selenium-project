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
    steps.fill_out_mandatory_fields(data = GLData.numbers)
    self.assertTrue(steps.is_save_button_enabled())

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

  def test_1_project_invalid_url_validation(self):
    pass

  def test_2_project_valid_url_validation(self):
    pass


class Certificates_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.CERTIFICATES)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_non_pdf_file_upload(self):
    pass
  def test_2_certificate_url_validation(self):
    pass
  def test_3_gif_upload_validation(self):
    pass
  def test_4_svg_upload_validation(self):
    pass
  def test_5_module_with_valid_data(self):
    pass


class Skills_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.SKILLS)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_input_field_for_many_chars(self):
    pass
  def test_2_add_same_skill_twice(self):
    pass
  def test_3_add_skills_limit(self):
    pass
  def test_4_skills_sorting(self):
    pass


class ContactInfo_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.EDUCATION)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_invalid_phone_number_validation(self):
    pass
  def test_2_valid_phone_number_validation(self):
    pass
  def test_3_send_code_button(self):
    pass

  def test_4_invalid_email_validation(self):
    pass
  def test_5_valid_email_validation(self):
    pass
  def test_6_send_code_to_registered_email(self):
    pass
  def test_7_send_code_button(self):
    pass
  def test_8_socials_with_invalid_url_format(self):
    pass
  def test_9_socials_with_valid_url_format(self):
    pass




class CV_Upload_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(ProfileLocators.MY_CV)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_upload_big_size_pdf_file(self):
    pass
  def test_2_upload_file_with_too_many_chars(self):
    pass
  def test_3_upload_non_pdf_file(self):
    pass
  def test_4_cv_update(self):
    pass

class Meet_User_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(ProfileLocators.MY_CV)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_valid_youtube_url(self):
    pass
  def test_2_invalid_youtube_url(self):
    pass
  def test_3_valid_video_file_type(self):
    pass
  def test_4_invalid_video_file_type(self):
    pass

if __name__ == '__main__':
  unittest.main()


