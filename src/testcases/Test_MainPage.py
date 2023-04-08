import unittest
from src.Main.TestSteps import Steps_MainPage
from src.testcases.TestSetup.Setup_BaseTest import BaseSetupClass
from src.testcases.TestSetup.TestDescription import description


class MainPageTest(BaseSetupClass):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.steps = Steps_MainPage.MainPage(cls.driver)


  #test whetever we get error messeage or not for searching for a vacancy that can't be found
  def test_1_vacancy_filter(self):
    self.steps.search_vacancy(text='abc123')
    result = self.steps.vacancy_not_found()
    self.assertTrue('შედეგი არ მოიძებნა' in result)

  def test_2_search_by_invalid_city(self):
    pass

  def test_3_save_vacancy(self):
    pass

  def test_4_


if __name__ == '__main__':
  unittest.main()