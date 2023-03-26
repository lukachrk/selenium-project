from dataclasses import dataclass, asdict
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class Card_locators:
    PROFILE_UPDATE: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[2]/div[4]/div/div/div"
    WORK_EXPERIENCE: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[3]/div[1]/div"
    EDUCATION: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[4]/div[1]/div"
    PROJECTS: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[5]/div[1]/div"
    KNOW_USER: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[3]/div[1]/div"
    SKILLS: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[5]/div[1]/div"
    LANGUAGES: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[6]/div[1]/div"
    CERTIFICATES: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[7]/div[1]/div"
    ADDRESS: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[4]/div[2]/div[2]"
    PHONE_NUMBER: str = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[4]/div[3]/div[2]"
    EMAIL: str = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[4]/div[4]/div[2]"
    SOCIALS: str = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[4]/div[5]/div[2]"


@dataclass
class Module_locators:
    NAME: tuple = By.ID, 'first_name'
    SURNAME: tuple = By.ID, 'last_name'
    PROFESSION: tuple = By.ID, 'title'
    UNIVERSITY: tuple = By.ID, 'institution'
    FACULTY: tuple = By.ID, 'faculty'
    DEGREE: tuple = By.ID, 'degree'
    GPA: tuple = By.ID, 'grade'
    POSITION: tuple = By.ID, 'position'
    EMPLOYER: tuple = By.ID, 'employer'
    FACEBOOK: tuple = By.ID, 'facebook'
    TWITTER: tuple = By.ID, 'twitter'
    LINKEDIN: tuple = By.ID, 'linkedin'
    DRIBBLE: tuple = By.ID, 'dribble'
    BEHANCE: tuple = By.ID, 'behance'
    OTHER: tuple = By.ID, 'other'


