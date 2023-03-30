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
		field_element = FieldElements(self.driver,field)
		field_element.send_input(data)

	
	def fill_out_fields(self, data):
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


	#in built selenium Select can't be used on ng-select angular elements. this is my implementation
	def select_option(self, Type:str, date:tuple):
		options = self.element.options_fields

		for i in options:
			try:
				option_label = i.find_element(By.XPATH, f".//div[text() = 'აირჩიე {Type}']")
				if(option_label):
					time.sleep(2)
					i.click()
					self.driver.find_element(*date).click()
			except NoSuchElementException:
				pass
	
	def get_options_list(self, Type:str) -> list:
		options = self.element.options_fields
		for i in options:
			try:
				option_label = i.find_element(By.XPATH, f".//div[text() = 'აირჩიე {Type}']")
				if(option_label):
					time.sleep(2)
					i.click()
					time.sleep(2)
					option_elements = self.element.options_list
					names  = [span.text for span in names]
					return names
			except NoSuchElementException:
				pass
	
	def click_till_now_checkbox(self) -> None:
		self.element.click_until_now


	def is_save_button_enabled(self) -> bool:
		button = self.element.save_button
		return button.is_enabled()


	def field_has_validation(self, warning_type) -> bool:
		warning_element = self.element.invalid_format_warning

		if warning_element is not None:
			return warning_type in warning_element.text

		return False

	def profile_updated_succesfully(self):
		success = self.element.success_message
		if(success):
			return True

		return False

	def open_my_project_url(self) -> bool:
		self.element.click_my_project_url
		time.sleep(3)

		self.driver.switch_to.window(self.driver.window_handles[1])
		url = self.driver.current_url
		self.driver.switch_to.window(self.driver.window_handles[1])

		return url

	def upload_cv(self, file:str):
		self.element.upload_cv


