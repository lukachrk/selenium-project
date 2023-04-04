import unittest
from src.Main.TestData.Data_Registration import RegistrationData as RGData
from src.Main.TestData.secret_keys import SecretKeys as Skeys
from src.Main.TestSteps import Steps_Registration
from src.testcases.TestSetup.Setup_BaseTest import BaseSetupClass
from src.testcases.TestSetup.TestDescription import description
import time


class Registration_Test(BaseSetupClass):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.steps = Steps_Registration.Registration(cls.driver)
    cls.steps.navigate_to_registration()


  def setUp(self):
    time.sleep(2)


  @description('entering valid number in input field and checking for any warnings')
  def test_1_phone_input_field_validation_for_valid_number(self):
    self.steps.fill_out_phone_number(number = RGData.valid_phone_number)
    self.assertFalse(self.steps.got_warning(warningType = 'number'))


  
  @description('entering invalid number in input field and checking for invalid format warning')
  def test_2_phone_input_field_validation_for_invalid_number(self):
    self.steps.fill_out_phone_number(number = RGData.invalid_phone_number)
    warning = self.steps.got_warning(warningType = 'number')
    self.assertIn('მობილურის ნომრის ფორმატი არ არის სწორი, გთხოვთ გადაამოწმოთ', warning)


  @description('entering letters in input field and checking for invalid format warning')
  def test_3_phone_input_field_validation_for_text(self):
    self.steps.fill_out_phone_number(number = RGData.valid_name_surname)
    warning = self.steps.got_warning(warningType = 'number')
    self.assertIn('მობილურის ნომრის ფორმატი არ არის სწორი, გთხოვთ გადაამოწმოთ', warning)

  def test_4_password_seven_symbols(self):
    self.steps.fill_out_password(password = RGData.seven_symbols)
    warning = self.steps.got_warning(warningType = 'password')
    self.assertIn('პაროლი უნდა შედგებოდეს მინიმუმ 8 სიმბოლოსგან', warning)


  def test_5_password_eight_symbols(self):
    self.steps.fill_out_password(password = RGData.eight_symbols)
    warning = self.steps.got_warning(warningType = 'password')
    self.assertFalse(warning)


  def test_6_password_nine_symbols(self):
    self.steps.fill_out_password(password = RGData.nine_symbols)
    warning = self.steps.got_warning(warningType = 'password')
    self.assertFalse(warning)

  @description('leaving every mandatory field empty and checking for warnings')
  def test_7_mandatory_fields(self):
    self.steps.fill_out_phone_number(number = RGData.leave_empty)
    phone = self.steps.field_is_mandatory(field = 'phone')
    self.assertIn('მობილურის ნომერი სავალდებულოა', phone)

    self.steps.fill_out_password(password = RGData.leave_empty)
    password = self.steps.field_is_mandatory(field = 'password')
    self.assertIn('პაროლი სავალდებულოა', password)

    self.steps.fill_out_name_surname(name = RGData.leave_empty)
    name = self.steps.field_is_mandatory(field = 'name')
    self.assertIn('სახელი და გვარი სავალდებულოა', name)


  @description('entering already registered user credentials')
  def test_8_registration_with_already_registered_user_data(self):
    self.steps.fill_out_phone_number(number=Skeys.phone_number)
    self.steps.fill_out_password(password=RGData.eight_symbols)
    self.steps.fill_out_name_surname(name = RGData.valid_name_surname)
    self.steps.click_terms_checkbox()
    self.steps.click_continue()

    warning = self.steps.got_warning(warningType = 'user')
    self.assertIn('ასეთი მომხმარებელი უკვე არსებობს', warning)


if __name__ == '__main__':
  unittest.main()