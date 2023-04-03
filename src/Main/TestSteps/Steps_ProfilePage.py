from src.Main.PageObject.Elements.Elements_ProfilePage import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import typing
import time

class Profile:
	def __init__(self, driver):
		self.driver = driver
		self.element = ProfileElements(self.driver)
	
	def navigate_to(self, navlink:str) -> None: 
		result = self.element.nav_links
		links = {elem.text: elem for elem in result}

		self.driver.implicitly_wait(10)
		links[navlink].click()


	def open_card(self, Card:str) -> None:
		card_element = CardElements(self.driver, Card)
		card_element.open_module()


	def close_module(self) -> None:
		self.element.close_button


	def save_changes(self) -> None:
		self.element.save_button


	def fill_out_field(self, field:str, data) -> None:
		field_element = FieldElements(self.driver, field)
		field_element.send_input(data)

	
	def fill_out_fields(self, data) -> None:
		input_fields = self.element.all_input_fields
		for i in input_fields:
			i.clear()
			i.send_keys(data)


	def fill_out_mandatory_fields(self, data) -> None:
		fields = self.element.mandatory_fields

		for i in fields:
			try:
				mandatory_text = i.find_element(By.XPATH, ".//small")
				if(mandatory_text):
					input_field = i.find_element(By.XPATH, ".//input")
					input_field.clear()
					input_field.send_keys(data)
			except NoSuchElementException:
				pass

	#helper function for opening dropdowns
	#in built selenium Select can't be used on ng-select angular elements. this is my implementation
	def click_option(self, Type:str):
		options = self.element.options_fields

		for i in options:
			try:
				option_label = i.find_element(By.XPATH, f".//div[text() = 'აირჩიე {Type}']")
				if(option_label):
					time.sleep(2)
					i.click()
			except NoSuchElementException:
				pass
	
	def get_option_names(self, Type:str) -> list:
		self.click_option(Type = Type)
		names = self.element.options_field_names
		return [name.text for name in names]
	
	
	def click_till_now_checkbox(self) -> None:
		self.element.click_until_now


	def is_save_button_enabled(self) -> bool:
		button = self.element.save_button
		return button.is_enabled()


	def field_has_validation(self, warning_type) -> bool:
		warning_element = self.element.invalid_format_warning

		if warning_element is not None:
			return warning_type in warning_element.text
		else:
			return False

	def module_updated_succesfully(self):
		success = self.element.success_message
		if(success):
			return True

		return False

	def open_my_project_url(self) -> bool:
		self.element.click_my_project_url
		time.sleep(3)

		self.driver.switch_to.window(self.driver.window_handles[1])
		url = self.driver.current_url
		self.driver.switch_to.window(self.driver.window_handles[0])

		return url

	def upload_cv(self, file:str):
		time.sleep(2)
		self.element.upload_cv = file
		

	def delete_cv(self):
		self.element.delete_cv
		self.element.click_yes

	def update_youtube_url(self, url:str,):
		self.element.options_fields[0].click()
		youtube_option = self.element.option_field_items[0].click()
		self.element.youtube_url = url


	def upload_video(self, path:str):
		self.element.options_fields[0].click()
		video_option = self.element.option_field_items[1].click()

		time.sleep(2)
		self.element.video_upload = path
		time.sleep(10)

	def click_send_code(self, element):
		send_button = FieldElements(self.driver, element)
		warning = self.element.user_registered_warning

		if(warning):
			return warning.text
		else:
			return None

	def add_skill(self, skill:str):
		self.element.options_fields[0].click()
		self.element.add_skill = skill
	
	def get_skills_list(self):
		skills_list = self.element.skills_list
		skill_names = skills_list.find_elements(By.TAG_NAME, 'span')
		return [names.text for names in skill_names]
			
	def upload_certificate(self, name:str, file:str, Type:str):
		self.element.certificate_name = name
		self.element.options_fields[0].click()
		upload_options = self.element.option_field_items

		if(Type=='pdf'):
			upload_options[0].click()
		else:
			upload_options[1].click()
			
		self.element.upload_certificate = file
	

	def fill_certificate_url(self, name, url):
		pass

	def invalid_format_warning(self) -> str:
		warning = self.element.invalid_format_warning
		if(warning):
			return warning.text
		else:
			return False

	def invalid_cv_warning(self) -> str:
		warning = self.element.invalid_cv_warning
		if(warning):
			return warning.text
		else:
			return False




