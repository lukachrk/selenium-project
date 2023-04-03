import unittest
from src.Main.TestSteps import Steps_Registration
from src.testcases.TestSetup.Setup_BaseTest import BaseSetupClass
from src.testcases.TestSetup.TestDescription import description


class Registration_Test(BaseSetupClass):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.steps = Steps_Registration.Registration(cls.driver)
    

if __name__ == '__main__':
  unittest.main()