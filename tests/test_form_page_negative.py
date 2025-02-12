import time
import pytest

from selenium.webdriver.common.by import By
from selenium import webdriver

from page_objects.form_page import FormPage
from page_objects.base_page import BasePage


class TestNegativeScenarios:

    name = "Greg"
    last_name = "Plow"
    mail = "g.p@gmail.com"
    gender = "Male"
    phone_number = "1112223334"
    subject = "Maths"
    hobbies = "Sports"
    address = "Kraków, Poland"
    state_and_city = "NCR Delhi"

    @pytest.mark.form
    @pytest.mark.negative
    def test_negative_name(self, driver):
        form_page = FormPage(driver)

        # Open page
        form_page.open()

        # Input incorrect 
        form_page.input_data("", self.last_name, self.mail, self.phone_number, self.subject, self.address)
        # Push Submit button
        form_page.submit_form()

        base_page = BasePage(driver)
        assert form_page.wait_for_css_property(form_page._first_name_field, "border-color", "rgb(220, 53, 69)") == "rgb(220, 53, 69)" , "Wrong border-color of name input, should be #dc3545"

    @pytest.mark.form
    @pytest.mark.negative
    def test_negative_last_name(self, driver):
        form_page = FormPage(driver)

        # Open page
        form_page.open()

        # Input incorrect 
        form_page.input_data(self.name, "", self.mail, self.phone_number, self.subject, self.address)
        # Push Submit button
        form_page.submit_form()

        base_page = BasePage(driver)
        assert form_page.wait_for_css_property(form_page._last_name_field, "border-color", "rgb(220, 53, 69)") == "rgb(220, 53, 69)" , "Wrong border-color of last name input, should be #dc3545"

    @pytest.mark.form
    @pytest.mark.negative
    def test_negative_email(self, driver):
        form_page = FormPage(driver)

        # Open page
        form_page.open()

        # Input incorrect 
        form_page.input_data(self.name, self.last_name, "abc", self.phone_number, self.subject, self.address)
        # Push Submit button
        form_page.submit_form()

        base_page = BasePage(driver)
        assert form_page.wait_for_css_property(form_page._email_field, "border-color", "rgb(220, 53, 69)") == "rgb(220, 53, 69)" , "Wrong border-color of e-mail input, should be #dc3545"

    @pytest.mark.form
    @pytest.mark.negative
    def test_negative_phone_number(self, driver):
        form_page = FormPage(driver)

        # Open page
        form_page.open()

        # Input incorrect 
        form_page.input_data(self.name, self.last_name, self.mail, "111222333", self.subject, self.address)
        # Push Submit button
        form_page.submit_form()

        base_page = BasePage(driver)
        assert form_page.wait_for_css_property(form_page._mobile_number_field, "border-color", "rgb(220, 53, 69)") == "rgb(220, 53, 69)", "Wrong border-color of mobile number input, should be #dc3545"

    @pytest.mark.form
    @pytest.mark.negative
    def test_gender_label(self, driver):
        form_page = FormPage(driver)

        # Open page
        form_page.open()

        # Input incorrect 
        form_page.input_data(self.name, self.last_name, self.mail, "111222333", self.subject, self.address)
        # Push Submit button
        form_page.submit_form()

        base_page = BasePage(driver)

        assert form_page.wait_for_css_property(form_page._gender_male_field, "color", "rgba(40, 167, 69, 1)") == "rgba(40, 167, 69, 1)", "Wrong color of gender label, should be #28a745"