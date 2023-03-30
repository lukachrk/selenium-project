from dataclasses import dataclass

@dataclass(frozen=True)
class generaldata:
  numbers: int = 1233454
  spacings: str = '      '
  leave_empty: str = ''
  symbols: str = '$%^&*'
  too_many_chars: str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
  spaced_letters: str = 'luka chrk'
  invalid_format = "შეყვანილი მონაცემები არ არის ვალიდური, გთხოვთ გადაამოწმოთ"
  invalid_url = "abc^.com"
  