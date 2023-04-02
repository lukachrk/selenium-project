from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass(frozen=True)
class ProfileLocators:
	NAVIGATION_LINKS: tuple = (By.XPATH, 
	"//div[contains(concat(' ', normalize-space(@class), ' '), ' profile-nav-link')]")

	#GENERAL ELEMENTS THAT ALL MODULES SHARE
	#save module button
	SAVE_BUTTON: tuple = By.XPATH, "//button[text() = ' შენახვა ']"

	#close module button
	CLOSE_BUTTON: tuple = By.XPATH, "//button[contains(@class, 'btn-close')]"

	ALL_INPUT_FIELD: tuple = By.XPATH, "//div[contains(@class, 'row')]/div[contains(@class, 'col-md-6')]/div/input"

	#module dropdowns
	DROPDOWNS: tuple = By.XPATH, "//ng-select"

	FORM_CHECK: tuple = By.XPATH, "//label[contains(@class, 'form-check-label')]"

	#invalid format text warning
	INVALID_FORMAT: tuple = By.XPATH, "//small[contains(@class, 'color-hot')]"
	
	MANDATORY_FIELDS: tuple = By.XPATH, "//div[contains(@class, 'form-group mb')]"

	OPTION_FIELDS: tuple = By.XPATH, "//ng-select"
	OPTION_FIELD_ITEMS: tuple = By.XPATH, "//div[contains(@class, 'ng-option')]"
	OPTION_FIELD_NAMES: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel')]/div/div/span"
	OPTION_UNTIL_NOW: tuple = By.ID, "flexCheckDefault"
	

	MANDATORY_OPTION_FROM:tuple = By.XPATH, "//label[text() = ' დან ']/small"
	MANDATORY_OPTION_TO:tuple = By.XPATH, "//label[text() = ' მდე ']/small"

	SUCCCESS_ALERT:tuple = By.XPATH, "//div[text() = ' შენი პროფილი წარმატებით განახლდა ' ]"

	MY_PROJECT_URL: tuple = By.XPATH, "//div[contains(@class, 'company-position')]/div/a"

	year_23: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel')]/div/div[1]"
	year_22: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel')]/div/div[2]"
	year_21: tuple = By.XPATH, "//div[contains(@class, 'ng-dropdown-panel')]/div/div[3]"



@dataclass(frozen=True)
class Card_locators:
	PROFILE_UPDATE: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[2]/div[4]/div/div/div"
	WORK_EXPERIENCE: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[3]/div[1]/div"
	EDUCATION: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[4]/div[1]/div"
	PROJECTS: tuple = By.XPATH, "//div[contains(@class, 'col-md-7')]/div[5]/div[1]/div"
	INTRO: tuple = By.XPATH, "//div[contains(@class, 'col-md-5')]/div[3]/div[1]/div"
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
	PROJECT_NAME: tuple = By.XPATH, "//div[contains(@class, 'form-group mb-3')]/input"
	PROJECT_URL: tuple = By.XPATH, "//div[contains(@class, 'form-group mb-3 mt-3')]/input"
	FACEBOOK: tuple = By.ID, 'facebook'
	TWITTER: tuple = By.ID, 'twitter'
	LINKEDIN: tuple = By.ID, 'linkedin'
	DRIBBLE: tuple = By.ID, 'dribble'
	BEHANCE: tuple = By.ID, 'behance'
	OTHER: tuple = By.ID, 'other'
	CV_UPLOAD: tuple = By.XPATH, "(//input[@type = 'file'])[2]"
	YOUTUBE_INPUT: tuple = By.ID, "video_url"
	VIDEO_UPLOAD: tuple = By.XPATH, "(//input[@type = 'file'])[3]"
	PHONE_INPUT: tuple = By.XPATH, "//div[contains(@class, 'input-group mb-3')]/input"
	EMAIL_INPUT: tuple = By.XPATH, "//div[contains(@class, 'input-group mb-3')]/input"
	SEND_CODE: tuple = By.XPATH, "//div[contains(@class, 'input-group mb-3')]/button"
	SKILL_INPUT: tuple = By.XPATH, "//div[contains(@class, 'ng-input')]/input"
	SKILLS_LIST: tuple = By.XPATH, "//div[contains(@class, 'col-12')]/div[contains(@class, 'gap-2')]"
	CERTIFICATE_INPUT: tuple = By.ID, 'name'
	CERTIFICATE_UPLOAD: tuple = By.XPATH, "(//input[@type = 'file'])[3]"
	CERTIFICATE_URL: tuple = By.ID, 'url'
	USER_ALREADY_REGISTERED: tuple = By.XPATH, "//div[text() = ' ასეთი მომხმარებელი უკვე არსებობს ']"
	INVALID_CV_WARNING: tuple = By.XPATH, "//div[text() = ' CV-ს ატვირთვა შესაძლებელია მხოლოდ PDF ფორმატში ' ]"


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
