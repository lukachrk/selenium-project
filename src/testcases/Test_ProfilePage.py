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

  def test_1_input_fields_against_numbers(self):
    steps.fill_out_fields(GLData.numbers)

  def test_2_input_fields_against_symbols(self):
    steps.fill_out_fields(GLData.symbols)




class Experience_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.WORK_EXPERIENCE)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_input_fields_against_numbers(self):
    steps.fill_out_fields(GLData.numbers)

  def test_2_input_fields_against_symbols(self):
    steps.fill_out_fields(GLData.symbols)  

  def test_3_input_fields_against_empty_spaces(self):
    steps.fill_out_fields(GLData.spacings)


  @description('filling out every mandatory field and checking if save button is enabled')
  def test_4_module_mandatory_fields(self):
    steps.fill_out_mandatory_fields(data = GLData.numbers)
    steps.select_option(Type=PFData.start_month, date=Months_locators.April)
    steps.select_option(Type=PFData.start_year, date=ProfileLocators.year_23)
    self.assertTrue(steps.is_save_button_enabled())

  @description('from and before time intervals shouldnt be same month')
  def test_5_select_options_month(self):
    steps.click_till_now_checkbox()
    steps.select_option(Type=PFData.start_month, date = Months_locators.March)
    options_list = steps.get_options_list(Type=PFData.end_month)

    self.assertNotIn('March', options_list)
  
  @description('if we start project in 2023, we shouldnt be able to choose 2022 as ending')
  def test_6_select_option_year(self):
    steps.click_till_now_checkbox()
    steps.select_option(Type=PFData.start_year, date = ProfileLocators.year_23)
    options_list = steps.get_options_list(Type=PFData.end_year)
    self.assertNotIn('2023', options_list)


class Education_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.EDUCATION)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_input_fields_against_symbols(self):
    steps.fill_out_fields(GLData.symbols)  

  def test_2_input_fields_against_empty_spaces(self):
    steps.fill_out_fields(GLData.spacings)
  
  def test_4_mandatory_fields(self):
    steps.fill_out_mandatory_fields(data = GLData.spaced_letters)

  def test_5_select_options_year(self):
    steps.select_option(Type=PFData.start_year, date = ProfileLocators.year_23)
    options_list = steps.get_options_list(Type=PFData.end_year)
    self.assertNotIn('2023', options_list)

  def test_module_for_valid_data(self):
    steps.fill_out_field(Module_locators.UNIVERSITY, data = PFData.university)
    steps.fill_out_field(Module_locators.FACULTY, data = PFData.faculty)
    steps.fill_out_field(Module_locators.DEGREE, data = PFData.degree)
    steps.fill_out_field(Module_locators.GPA, data = PFData.gpa)
    steps.select_option(Type = PFData.start_year, date = ProfileLocators.year_22)

    steps.save_changes()
    self.assertTrue(steps.profile_updated_succesfully())


class Project_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.PROJECTS)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_project_invalid_url_validation(self):
    steps.fill_out_field(Module_locators.PROJECT_NAME, data = GLData.spaced_letters)

    steps.select_option(Type = PFData.start_month, date = ProfileLocators.year_21)
    steps.select_option(Type = PFData.start_year, date = Months_locators.March)

    steps.fill_out_field(Module_locators.PROJECT_URL, data = GLData.invalid_url)
    self.assertFalse(steps.is_save_button_enabled())


  def test_2_module_for_valid_data(self):
    steps.fill_out_field(Module_locators.PROJECT_NAME, data = PFData.project_name)

    steps.select_option(Type = PFData.start_month, date = ProfileLocators.year_21)
    steps.select_option(Type = PFData.start_year, date = Months_locators.March)

    steps.fill_out_field(Module_locators.PROJECT_URL, data = PFData.project_url)

    steps.close_module()
    url = steps.open_my_project_url()
    steps.open_card(Card_locators.PROJECTS)

    self.assertIn(PFData.project_url, url)


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
    steps.upload_cv(file = PFData.big_pdf)

  def test_2_upload_file_with_long_name(self):
    steps.upload_cv(file = PFData.longName_pdf)

  def test_3_upload_non_pdf_file(self):
    steps.upload_cv(file = PFData.docx_file)

  def test_4_valid_pdf_file(self):
    steps.upload_cv(file = PFData.cv)

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


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Experience_Module_Test))
    return test_suite

mySuit=suite()



if __name__ == '__main__':
  runner=unittest.TextTestRunner()
  runner.run(mySuit)


