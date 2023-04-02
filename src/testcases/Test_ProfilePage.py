import unittest
from src.Main.TestData.Data_ProfilePage import ProfileData as PFData
from src.Main.TestData.Data_General import generaldata as GLData
from src.Main.PageObject.Locators.Locators_ProfilePage import *

from src.testcases.TestSetup.TestDescription import description
from src.testcases.TestSetup.ProfileSetup import *
import time

"""
no setupclass, since we don't open any modules but rather just cheking the nav links
when test finishes execution, return to profile to continue modules testing
"""
class ProfilePage_Test(unittest.TestCase):
  @classmethod
  def tearDownClass(cls):
    steps.navigate_to(navlink = 'პროფილი')

  def test_navigation(self):
    steps.navigate_to(navlink='პროფილი')
    self.assertIn('nav=profile', self.driver.current_url) 

    steps.navigate_to(navlink='გაგზავნილი აპლიკაციები')
    self.assertIn('nav=sent', self.driver.current_url)    

    steps.navigate_to(navlink='შენახული ვაკანსიები')
    self.assertIn('nav=saved', self.driver.current_url)    

    steps.navigate_to(navlink='სამუშაოს შეტყობინებები')
    self.assertIn('nav=job_alerts', self.driver.current_url)    

    steps.navigate_to(navlink='პარამეტრები')
    self.assertIn('nav=settings', self.driver.current_url)



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

  @description('entering numbers in position module fields and checking if it validates')
  def test_1_input_fields_against_numbers(self):
    steps.fill_out_fields(GLData.numbers)

  @description('entering symbols in position module fields and checking if it validates')
  def test_2_input_fields_against_symbols(self):
    steps.fill_out_fields(GLData.symbols)  

  @description('entering empty spaces in position module fields and checking if it validates')
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
  
  def test_3_mandatory_fields(self):
    steps.fill_out_mandatory_fields(data = GLData.spaced_letters)

  @description('if we start project in 2023, we shouldnt be able to choose 2022 as ending')
  def test_4_select_options_year(self):
    steps.select_option(Type=PFData.start_year, date = ProfileLocators.year_23)
    options_list = steps.get_options_list(Type=PFData.end_year)
    self.assertNotIn('2023', options_list)

  @description('filling out every field with valid data and checking if it saves')
  def test_module_for_valid_data(self):
    steps.fill_out_field(Module_locators.UNIVERSITY, data = PFData.university)
    steps.fill_out_field(Module_locators.FACULTY, data = PFData.faculty)
    steps.fill_out_field(Module_locators.DEGREE, data = PFData.degree)
    steps.fill_out_field(Module_locators.GPA, data = PFData.gpa)
    steps.select_option(Type = PFData.start_year, date = ProfileLocators.year_22)

    steps.save_changes()
    self.assertTrue(steps.module_updated_succesfully())


class Project_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.PROJECTS)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description('entering random letters as url in project url field')
  def test_1_project_invalid_url_validation(self):
    steps.fill_out_field(Module_locators.PROJECT_NAME, data = GLData.spaced_letters)

    steps.select_option(Type = PFData.start_month, date = ProfileLocators.year_21)
    steps.select_option(Type = PFData.start_year, date = Months_locators.March)

    steps.fill_out_field(Module_locators.PROJECT_URL, data = GLData.invalid_url)
    self.assertFalse(steps.is_save_button_enabled())

  @description('filling out every field with valid data and checking if project link works')
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

  @description('checking file validation by uploading non pdf file as certificate')
  def test_1_non_pdf_file_upload(self):
    cer_name = GLData.spaced_letters
    cer_type = 'pdf'
    cer_file = PFData.docx_file
    steps.upload_certificate(cer_name, cer_file, cer_type)

    self.assertFalse(steps.is_save_button_enabled())

  @description('checking url validation for certificate')
  def test_2_certificate_url_validation(self):
    steps.fill_out_field(field = Module_locators.CERTIFICATE_URL, data = GLData.numbers)
    self.assertFalse(steps.is_save_button_enabled())

  def test_3_module_with_valid_data(self):
    pass


class Skills_Module_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.SKILLS)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description('entering too long characters into skill input field')
  def test_1_input_field_for_many_chars(self):
    steps.add_skill(skill = GLData.too_many_chars)
    skills = steps.get_skills_list()
    self.assertLess(len(skills), 1)

  @description('entering same skill twice and cheking if it gets added')
  def test_2_add_same_skill_twice(self):
    steps.add_skill(skill = PFData.profession)
    steps.add_skill(skill = PFData.profession)
    skills = steps.get_skills_list()
    self.assertEquals(len(skills), 1)
    
  @description('entering symbols as a skill of the user and check if it gets added')
  def test_3_add_skills_against_symbols(self):
    steps.add_skill(skill = GLData.symbols)

    skills = steps.get_skills_list()
    self.assertLess(len(skills), 1)

  @description('entering numbers as a skill of the user and check if it gets added')
  def test_4_add_skills_against_numbers(self):
    steps.add_skill(skill = GLData.numbers)

    skills = steps.get_skills_list()
    self.assertLess(len(skills), 1)

"""
contact info module isn't one module but rather wrapper around small sub-modules
the way how modules open should be handled from method to method
thus not having setupclass in this test class
"""
class ContactInfo_Module_Test(unittest.TestCase):
  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  @description('entering random numbers in phone field and checking for validation')
  def test_1_invalid_phone_number_validation(self):
    steps.open_card(Card_locators.PHONE_NUMBER)
    steps.fill_out_field(field = Module_locators.PHONE_INPUT, data = GLData.numbers)

    got_warning = steps.invalid_format_warning()
    self.assertTrue(got_warning)

  @description('entering valid georgian phone number format and cheking for validation')
  def test_2_valid_phone_number_validation(self):
    steps.close_module()
    steps.fill_out_field(field = Module_locators.PHONE_INPUT, data = GLData.numbers)

    got_warning = steps.invalid_format_warning()
    self.assertFalse(got_warning)

  @description('entering invalid email format in input field and checking for validation')
  def test_3_invalid_email_validation(self):
    steps.open_card(Card_locators.EMAIL)
    steps.fill_out_field(field = Module_locators.EMAIL_INPUT, data = PFData.invalid_email)

    got_warning = steps.invalid_format_warning()
    self.assertTrue(got_warning)

  def test_4_valid_email_validation(self):
    steps.fill_out_field(field = Module_locators.EMAIL_INPUT, data = PFData.valid_email)

  @description('sending email verification code to already registered email')
  def test_5_send_code_to_registered_email(self):
    steps.fill_out_field(field = Module_locators.EMAIL_INPUT, data = PFData.valid_email)

    warning = steps.click_send_code(Module_locators.SEND_CODE)
    self.assertIn('ასეთი მომხმარებელი უკვე არსებობს ', warning)

    steps.close_module()

  @description('filling out every social media link with google.com and checking for validation')
  def test_6_socials_with_invalid_url_format(self):
    steps.open_card(Card_locators.SOCIALS)
    steps.fill_out_fields(data = PFData.other_url)
    self.assertFalse(steps.is_save_button_enabled())

  def test_7_socials_against_numbers(self):
    steps.fill_out_fields(data = GLData.numbers)
    self.assertFalse(steps.is_save_button_enabled())

  def test_8_socials_against_symbols(self):
    steps.fill_out_fields(data = GLData.numbers)
    self.assertFalse(steps.is_save_button_enabled())

  def test_9_socials_against_spaced_letters(self):
    steps.fill_out_fields(data = GLData.numbers)
    self.assertFalse(steps.is_save_button_enabled())

  def test_10_socials_against_many_chars(self):
    steps.fill_out_fields(data = GLData.numbers)
    self.assertFalse(steps.is_save_button_enabled())


class CV_Upload_Test(unittest.TestCase): 
  @description('files with more than 25mb should be filtered out from being uploaded')
  def test_1_upload_big_size_pdf_file(self):
    steps.upload_cv(file = PFData.big_pdf)

  @description('files with long names or specials symbols in their name should be filtered from uploading')
  def test_2_upload_file_with_long_name(self):
    steps.upload_cv(file = PFData.longName_pdf)

  @description('uploading docx file to cv')
  def test_3_upload_non_pdf_file(self):
    steps.upload_cv(file = PFData.docx_file)
    got_warning = steps.invalid_cv_warning()
    self.assertTrue(got_warning)

  @description('upload valid pdf file and check if it opens')
  def test_4_valid_pdf_file(self):
    steps.upload_cv(file = PFData.cv)


class Intro_Test(unittest.TestCase): 
  @classmethod
  def setUpClass(cls):
    time.sleep(3)
    steps.open_card(Card_locators.INTRO)

  @classmethod
  def tearDownClass(cls):
    steps.close_module()

  def test_1_valid_youtube_url(self):
    steps.update_youtube_url(url = PFData.valid_yt_url)
    got_warning = steps.invalid_format_warning()
    self.assertFalse(got_warning)

  @description('entering invalid yt url in intro module')
  def test_2_invalid_youtube_url(self):
    steps.update_youtube_url(url = PFData.invalid_yt_url)
    warning = steps.invalid_format_warning()
    self.assertIn('YouTube-ის ლინკი არასწორია', warning)

  @description('uploading supported mp4 video file as a intro')
  def test_3_valid_video_file_type(self):
    steps.upload_video(path = PFData.valid_video)
    self.assertTrue(steps.is_save_button_enabled())

  @description('uploading unsupported gif file as intro video ')
  def test_4_invalid_video_file_type(self):
    steps.upload_video(path = PFData.invalid_video)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Intro_Test))
    return test_suite

mySuit=suite()



if __name__ == '__main__':
  runner=unittest.TextTestRunner()
  runner.run(mySuit)


