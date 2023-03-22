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