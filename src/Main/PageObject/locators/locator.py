from selenium.webdriver.common.by import By

class authPageLocators:
  Login_button = (By.CLASS_NAME, 'btn.color-base.login-btn.font-bold.ng-tns-c78-1.ng-star-inserted')

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

  #elements: work experience, education, projects, get to know user, skills, languages, certificates
  PROFILE_CARDS = {
    'ჩემს შესახებ' : "//div[contains(@class, 'col-md-7')]/div[2]/div[4]/div/div/div",
    'სამუშაო გამოცდილება' : "//div[contains(@class, 'col-md-7')]/div[3]/div[1]/div",
    'განათლება' : "//div[contains(@class, 'col-md-7')]/div[4]/div[1]/div",
    'პროექტები' : "//div[contains(@class, 'col-md-7')]/div[5]/div[1]/div",
    'გაიცანი მომხმარებელი' : "//div[contains(@class, 'col-md-5')]/div[3]/div[1]/div",
    'უნარები' : "//div[contains(@class, 'col-md-5')]/div[5]/div[1]/div",
    'ენები' : "//div[contains(@class, 'col-md-5')]/div[6]/div[1]/div",
    'სერტიფიკატები' : "//div[contains(@class, 'col-md-5')]/div[7]/div[1]/div",
    'მისამართი' : "//div[contains(@class, 'col-md-5')]/div[4]/div[2]/div[2]",
    'ნომერი' : "//div[contains(@class, 'col-md-5')]/div[4]/div[3]/div[2]",
    'ელფოსტა' : "//div[contains(@class, 'col-md-5')]/div[4]/div[4]/div[2]",
    'სოცქსელები' : "//div[contains(@class, 'col-md-5')]/div[4]/div[5]/div[2]"
    }
  #cv upload card
  MY_CV = (By.XPATH, "//div[contains(@class, 'col-md-5')]/div[2]")

  #GENERAL ELEMENTS THAT ALL MODULES SHARE
  #modules save button
  SAVE_BUTTON = (By.XPATH, "//div[text() = 'შენახვა']")

  #module dropdowns
  DROPDOWNS = (By.XPATH, "//ng-select")

  #form check
  FORM_CHECK = (By.XPATH, "//label[contains(@class, 'form-check-label')]")

  #individual module elements
  MODULE_ELEMENTS = {
    'about_module':[
      {'NAME':(By.ID, 'first_name')},
      {'SURNAME': (By.ID, 'last_name')},
      {'PROFESSION': (By.ID, 'title')},
    ],
    'education':[
      {'UNIVERSITY': (By.ID, 'institution')},
      {'FACULTY': (By.ID, 'faculty')},
      {'DEGREE': (By.ID, 'degree')},
      {'GPA': (By.ID, 'grade')}
    ],
    'work_experience':[
      {'NAME_URL': (By.ID, 'title')},
    ],
    'socials':[
      {'FACEBOOK': (By.ID, 'facebook')},
      {'TWITTER': (By.ID, 'twitter')},
      {'LINKEDIN': (By.ID, 'linkedin')},
      {'DRIBBLE': (By.ID, 'dribble')},
      {'BEHANCE': (By.ID, 'behance')},
      {'OTHER': (By.ID, 'other')}
    ]
  }



