from selenium.webdriver.common.by import By

class authPageLocators:
  Login_button = (By.XPATH, "//button[text()=' შესვლა ']")

  EMAIL_INPUT = (By.ID, 'floatingInput1')
  PASSWORD_INPUT = (By.ID, 'floatingInput2')
  
  AUTHORIZATION_BUTTON = (By.XPATH, "//button[text()=' ავტორიზაცია ']")
  AUTHORIZATION_ALERT = (By.XPATH, 
  "//div[text()=' ავტორიზაცია წარმატებულია ' or  text()=' მობილურის ნომერი ან პაროლი არასწორია ']")


class MainPageLocators:
  VACANCY_INPUT = (By.CLASS_NAME, 'form-control')
  VACANCY_SEARCH_BUTTON = (By.XPATH, '//app-search-panel/div/div[3]/button')
  VACANCY_RESULT_NULL = (By.XPATH, "//span[text()='შედეგი არ მოიძებნა']")

  POPUP = (By.CLASS_NAME, 'btn.btn-medium')
  NAVIGATION_LINKS = (By.XPATH, "//div[contains(@class, 'profile-nav-link')]/span[contains(@class, 'd-md-inline')]")

  HAMBURGER_DROPDOWN = (By.XPATH, "//div[contains(@class, 'header-account')]")
  HAMBURGER_APPLICATION_SENT = (By.XPATH, "//span[text() = 'გაგზავნილი აპლიკაციები']")


class ProfileLocators:
  NAVIGATION_LINKS = (By.XPATH, 
  "//div[contains(concat(' ', normalize-space(@class), ' '), ' profile-nav-link')]")

  #Edit buttons of Profile Page Cards 
  PROFILE_CARDS = {
    'PROFILE_UPDATE':  "//div[contains(@class, 'col-md-7')]/div[2]/div[4]/div/div/div",
    'WORK_EXPERIENCE':  "//div[contains(@class, 'col-md-7')]/div[3]/div[1]/div",
    'EDUCATION':  "//div[contains(@class, 'col-md-7')]/div[4]/div[1]/div",
    'PROJECTS':  "//div[contains(@class, 'col-md-7')]/div[5]/div[1]/div",
    'KNOW_USER':  "//div[contains(@class, 'col-md-5')]/div[3]/div[1]/div",
    'SKILLS':  "//div[contains(@class, 'col-md-5')]/div[5]/div[1]/div",
    'LANGUAGES':  "//div[contains(@class, 'col-md-5')]/div[6]/div[1]/div",
    'CERTIFICATES':  "//div[contains(@class, 'col-md-5')]/div[7]/div[1]/div",
    'ADDRESS':  "//div[contains(@class, 'col-md-5')]/div[4]/div[2]/div[2]",
    'PHONE_NUMBER':  "//div[contains(@class, 'col-md-5')]/div[4]/div[3]/div[2]",
    'EMAIL':  "//div[contains(@class, 'col-md-5')]/div[4]/div[4]/div[2]",
    'SOCIALS':  "//div[contains(@class, 'col-md-5')]/div[4]/div[5]/div[2]"
    }
  #cv upload card
  MY_CV = (By.XPATH, "//div[contains(@class, 'col-md-5')]/div[2]")

  #GENERAL ELEMENTS THAT ALL MODULES SHARE
  #modules save button
  SAVE_BUTTON = (By.XPATH, "//button[text() = ' შენახვა ']")

  #modules close button
  CLOSE_BUTTON = (By.CLASS_NAME, "btn-close")

  #module dropdowns
  DROPDOWNS = (By.XPATH, "//ng-select")

  #form check
  FORM_CHECK = (By.XPATH, "//label[contains(@class, 'form-check-label')]")

  #invalid format text
  INVALID_FORMAT = (By.XPATH, "//small[contains(@class, 'color-hot')]")

  #individual module input field elements
  MODULE_ELEMENTS = {
    'profile_update':{
      'NAME':(By.ID, 'first_name'),
      'SURNAME': (By.ID, 'last_name'),
      'PROFESSION': (By.ID, 'title'),
    },
    'education':{
      'UNIVERSITY': (By.ID, 'institution'),
      'FACULTY': (By.ID, 'faculty'),
      'DEGREE': (By.ID, 'degree'),
      'GPA': (By.ID, 'grade')
    },
    'work_experience':{
      'POSITION': (By.ID, 'position'),
      'EMPLOYER': (By.ID, 'employer'),
    },
    'socials':{
      'FACEBOOK': (By.ID, 'facebook'),
      'TWITTER': (By.ID, 'twitter'),
      'LINKEDIN': (By.ID, 'linkedin'),
      'DRIBBLE': (By.ID, 'dribble'),
      'BEHANCE': (By.ID, 'behance'),
      'OTHER': (By.ID, 'other')
    }
  }




