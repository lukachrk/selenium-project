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
  big_pdf:str = 'C:/Users/luka/Desktop/some.pdf'
  longName_pdf:str = 'C:/Users/luka/Desktop/APznzaahCkqx6SRDOEIJp346ViYc4GIfRvDMzm5XkwVh4LN--ny42HHK36zsAjgxBSrhk1d9YuC8nIlSdt6FFpZ7J-dGtj-gR62lj_UWJHgUUvvDArp01jVt9mx00UCn6fZC_mut7kFt9B1uYbt5MiArK-WrN21WZ9I7jD_d9ccCvqbPTj0U8Y36tqPeqM_r9vxZCVYlxSJrO44OhXC1jGA.pdf'
  docx_file:str = 'C:/Users/luka/Desktop/test.docx'
  cv:str = ''
  valid_yt_url: str = 'youtu.be/1'
  invalid_yt_url: str = 'youtu.be1'
  valid_video: str = 'C:/Users/luka/Desktop/certf.mp4'
  invalid_video: str = 'C:/Users/luka/Desktop/certf.gif'
  valid_email: str = 'someone@gmail.com'
  invalid_email: str = '1@gmail.com'
  valid_phone_number: str = '+995599000000'





