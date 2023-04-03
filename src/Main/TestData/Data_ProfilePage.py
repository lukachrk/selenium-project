from dataclasses import dataclass
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

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
  big_pdf:str = os.path.join(dir_path, 'Files', 'pdf-sample.pdf')
  longName_pdf:str = os.path.join(dir_path, 'Files', 'APznzaahCkqx6SRDOEIJp346ViYc4GIfRvDM.pdf')
  docx_file:str = os.path.join(dir_path, 'Files', 'test.docx')
  valid_yt_url: str = 'youtu.be/1'
  invalid_yt_url: str = 'youtu.be1'
  valid_video: str = os.path.join(dir_path, 'Files', 'test.mp4')
  invalid_video: str = os.path.join(dir_path, 'Files', 'test.gif')
  valid_email: str = 'someone@gmail.com'
  invalid_email: str = '1@gmail.com'
  valid_phone_number: str = '+995599000000'





