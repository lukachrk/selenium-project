from src.Main.TestSteps import Steps_Authentication
from src.Main.TestData.secret_keys import SecretKeys as SKEYS
from src.testcases.TestSetup.Setup_BaseTest import BaseSetupClass


class AuthTest(BaseSetupClass):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.steps = Steps_Authentication.AuthModule(cls.driver)
    cls.steps.open_auth_module()


  """
  decision table based test case to test authentication
  TF - Login(true), password(false)
  FT - Login(false), password(true)
  FF - Login(false), password(false)
  TT - Login(true), password(true)
  """


  def test_1_auth_TF(self):
    self.steps.send_credentials(login = SKEYS.login, password = SKEYS.invalid_password)
    result = self.steps.click_authorize()
    self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text)  
    
  def test_2_auth_FT(self):
    self.steps.send_credentials(login = SKEYS.invalid_login, password = SKEYS.Password)
    result = self.steps.click_authorize()
    self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text)  
    
  def test_3_auth_FF(self):
    self.steps.send_credentials(login = SKEYS.invalid_login, password = SKEYS.invalid_password)
    result = self.steps.click_authorize()
    self.assertIn('მობილურის ნომერი ან პაროლი არასწორია', result.text) 

  def test_4_auth_TT(self):
    self.steps.send_credentials(login = SKEYS.login, password = SKEYS.Password)
    result = self.steps.click_authorize()
    self.assertIn('ავტორიზაცია წარმატებულია', result.text)


if __name__ == '__main__':
  unittest.main()