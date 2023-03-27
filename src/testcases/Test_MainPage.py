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
  def test_vacancy_filter(self):
    result = self.steps.search_vacancy(text='abc123')
    self.assertTrue('შედეგი არ მოიძებნა' in result.text)


if __name__ == '__main__':
  unittest.main()