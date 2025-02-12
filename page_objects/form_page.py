from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

from page_objects.base_page import BasePage


class FormPage(BasePage):
    __url = "https://demoqa.com/automation-practice-form"
    _first_name_field = (By.ID, "firstName")
    _last_name_field = (By.ID, "lastName")
    _email_field = (By.ID, "userEmail")
    _gender_male_field = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    _mobile_number_field = (By.ID, "userNumber")
    __birth_date_field = (By.CSS_SELECTOR, "div[class='react-datepicker__input-container']")
    __date_picker_field = (By.CSS_SELECTOR, "div[class='react-datepicker__month'] div[class='react-datepicker__week']:nth-child(1) div:nth-child(1)")
    __subjects_field = (By.CSS_SELECTOR, ".subjects-auto-complete__control.css-yk16xz-control")
    __subject_input_locator = (By.ID, "subjectsInput")
    __hobbies_field = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    __current_adress_field = (By.ID, "currentAddress")
    __state_field = (By.XPATH, "//div[text()='Select State']")
    __state_field_list = (By.ID, "react-select-3-option-0")
    __city_field = (By.XPATH, "//div[text()='Select City']")
    __city_field_list = (By.ID, "react-select-4-option-0")
    __submit_button = (By.ID, "submit")
    __header_locator = (By.ID, "example-modal-sizes-title-lg")
    __student_name_locator = (By.XPATH, "//tr[td[text()='Student Name']]/td[2]")
    __student_email_locator = (By.XPATH, "//tr[td[text()='Student Email']]/td[2]")
    __student_gender_locator = (By.XPATH, "//tr[td[text()='Gender']]/td[2]")
    __student_mobile_locator = (By.XPATH, "//tr[td[text()='Mobile']]/td[2]")
    __student_subject_locator = (By.XPATH, "//tr[td[text()='Subjects']]/td[2]")
    __student_hobbies_locator = (By.XPATH, "//tr[td[text()='Hobbies']]/td[2]")
    __student_address_locator = (By.XPATH, "//tr[td[text()='Address']]/td[2]")
    __student_state_and_city_locator = (By.XPATH, "//tr[td[text()='State and City']]/td[2]")
    __close_summary_button_locator = (By.ID, "closeLargeModal")
    

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def input_data(self, firstname: str, lastname: str, email: str, mobilenumber, subjects: str, currentadress: str):
        super()._type(self._first_name_field, firstname)
        super()._type(self._last_name_field, lastname)
        super()._type(self._email_field, email)
        super()._click(self._gender_male_field)
        super()._type(self._mobile_number_field, mobilenumber)
        super()._click(self.__birth_date_field)
        super()._click(self.__date_picker_field)
        super()._autocompleteselect(self.__subjects_field, self.__subject_input_locator, subjects)
        super()._click(self.__hobbies_field)
        super()._type(self.__current_adress_field, currentadress)
        super()._autoselect(self.__state_field, self.__state_field_list)
        super()._autoselect(self.__city_field, self.__city_field_list)

    def submit_form(self):
        super()._click(self.__submit_button)

    def close_summary(self):
        super()._click(self.__close_summary_button_locator)


    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
    
    @property
    def name(self) -> str:
        return super()._get_text(self.__student_name_locator)
    
    @property
    def email(self) -> str:
        return super()._get_text(self.__student_email_locator)
    
    @property
    def gender(self) -> str:
        return super()._get_text(self.__student_gender_locator)
    
    @property
    def mobile_number(self) -> str:
        return super()._get_text(self.__student_mobile_locator)
    
    @property
    def subject(self) -> str:
        return super()._get_text(self.__student_subject_locator)
    
    @property
    def hobbies(self) -> str:
        return super()._get_text(self.__student_hobbies_locator)
    
    @property
    def address(self) -> str:
        return super()._get_text(self.__student_address_locator)
    
    @property
    def state_and_city(self) -> str:
        return super()._get_text(self.__student_state_and_city_locator)
    
    
    def wait_for_css_property(self, locator: tuple[str, str], property: str, expected_value: str, timeout: int = 10) -> str:
   
        def property_condition(driver):
            element = driver.find_element(*locator)
            return element.value_of_css_property(property) == expected_value

        WebDriverWait(self._driver, timeout).until(property_condition)
        
        return super()._get_value_of_css_property(locator, property, timeout)