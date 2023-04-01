from dataclasses import dataclass

@dataclass(frozen=True)
class ProfileData:
  valid_name: str = 'luka'
  invalid_name: int = '123'
  surname: str = 'def'
  invalid_surname: int = '456'
  profession: str = 'programmer'
  university: str = 'mit'
  faculty: str = 'compsci'
  degree: str = 'bachelor'
  gpa: int = '3.8'
  project_name: str = 'selenium project'
  project_url: str = 'https://github.com/lukachrk/selenium-project'
  facebook_url: str = 'https://www.facebook.com/123'
  twitter_url: str = 'https://twitter.com/home'
  linkedin_url: str = 'https://www.linkedin.com/feed/'
  dribble_url: str = 'https://dribbble.com/'
  behance_url: str = 'behance.net/'
  other_url: str = 'https://www.google.com/'
  start_month:str = 'დაწყების თვე'
  end_month:str = 'დასრულების თვე'
  start_year:str = 'დაწყების წელი'
  end_year:str = 'დასრულების წელი'
  big_pdf:str = ''
  longName_pdf:str = ''
  docx_file:str = ''
  cv:str = ''
  valid_yt_url: str = ''
  invalid_yt_url: str = ''
  valid_video: str = ''
  invalid_video: str = ''
  valid_email: str = ''
  invalid_email: str = ''





