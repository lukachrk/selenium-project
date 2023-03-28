from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class ProfileLocators:
	NAVIGATION_LINKS: tuple = (By.XPATH, 
	"//div[contains(concat(' ', normalize-space(@class), ' '), ' profile-nav-link')]")

	#upload cv card
	MY_CV: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[2]"

	#GENERAL ELEMENTS THAT ALL MODULES SHARE
	#save module button
	SAVE_BUTTON: tuple = By.XPATH, "//button[text() = ' შენახვა ']"

	#close module button
	CLOSE_BUTTON: tuple = By.CLASS_NAME, "btn-close"

	#module dropdowns
	DROPDOWNS: tuple = By.XPATH, "//ng-select"

	FORM_CHECK: tuple = By.XPATH, "//label[contains(@class, 'form-check-label')]"

	#invalid format text warning
	INVALID_FORMAT: tuple = By.XPATH, "//small[contains(@class, 'color-hot')]"
	
	MANDATORY_FIELDS: tuple = By.XPATH, "//div[contains(@class, 'form-group mb')]"
	
	OPTION_FIELDS: tuple = By.XPATH, "//ng-select"


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
	PHONE_NUMBER: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[4]/div[3]/div[2]"
	EMAIL: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[4]/div[4]/div[2]"
	SOCIALS: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[4]/div[5]/div[2]"


@dataclass(frozen=True)
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

@dataclass(frozen=True)
class Months_locators:
	January: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[1]"
	February: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[2]"
	March: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[3]"
	April: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[4]"
	May: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[5]"
	June: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[6]"
	July: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[7]"
	August: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[8]"
	September: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[9]"
	October: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[10]"
	November: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[11]"
	December: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel-items')]/div/div[12]"

