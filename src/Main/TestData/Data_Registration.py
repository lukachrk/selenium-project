from dataclasses import dataclass

@dataclass(frozen=True)
class RegistrationData:
  seven_symbols: str = 'drf23yk'
  eight_symbols: str = 'drf23yk3'
  nine_symbols: str = 'drf23ykg5'
  valid_phone_number: str = '+995599000000'
  invalid_phone_number: str = '12345'
  valid_name_surname: str = 'luka chrk'
  invalid_name_surname: str = 'lukachrk'
  leave_empty: str = ''