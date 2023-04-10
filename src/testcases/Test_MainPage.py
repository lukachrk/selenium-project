import unittest
from src.Main.TestSteps import Steps_MainPage, Steps_Authentication
from src.testcases.TestSetup.Setup_BaseTest import BaseSetupClass
from src.testcases.TestSetup.TestDescription import description
from src.Main.TestData.secret_keys import SecretKeys as Skeys

class MainPageTest(BaseSetupClass):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.steps = Steps_MainPage.MainPage(cls.driver)
    cls.auth = Steps_Authentication.AuthModule(cls.driver)


  @description('entering random letters/numbers and searching for vacancy')
  def test_1_vacancy_filter(self):
    self.steps.search_vacancy(text='abc123', city='თბილისი')
    result = self.steps.vacancy_not_found()
    self.assertTrue('შედეგი არ მოიძებნა' in result)
    self.steps.return_to_main_page()

  @description('entering random letters/numbers in city field and searching for vacancy')
  def test_2_search_by_invalid_city(self):
    self.steps.search_vacancy(text='programmer', city='123')
    result = self.steps.vacancy_not_found()
    self.assertTrue('შედეგი არ მოიძებნა' in result)
    self.steps.return_to_main_page()

  @description('bookmark vacancy as guest and test if it gets saved')
  def test_3_save_vacancy_as_guest(self):
    vacancy_to_save = self.steps.save_vacancy()
    self.auth.send_credentials(login = Skeys.login, password = Skeys.Password)
    self.auth.click_authorize()

    saved_vacancy = self.steps.check_for_saved_vacancy()
    self.assertTupleEqual(vacancy_to_save, saved_vacancy)

    self.steps.return_to_main_page()

  @description('bookmark vacancy as user and test if it gets saved')
  def test_4_save_vacancy_as_user(self):
    vacancy_to_save = self.steps.save_vacancy()
    saved_vacancy = self.steps.check_for_saved_vacancy()

    self.assertTupleEqual(vacancy_to_save, saved_vacancy)


if __name__ == '__main__':
  unittest.main()