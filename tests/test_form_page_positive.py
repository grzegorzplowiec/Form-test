import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

from page_objects.form_page import FormPage


class TestPositiveScenarios:

    name = "Greg"
    last_name = "Plow"
    mail = "g.p@gmail.com"
    gender = "Male"
    phone_number = "1112223334"
    subject = "Maths"
    hobbies = "Sports"
    adress = "Kraków, Poland"
    state_and_city = "NCR Delhi"

    @pytest.mark.form
    @pytest.mark.positive
    def test_positive_input(self, driver: WebDriver | WebDriver | WebDriver):
        form_page = FormPage(driver)

        # Open page
        form_page.open()
        # Input correct data
        form_page.input_data(self.name, self.last_name, self.mail, self.phone_number, self.subject, self.adress)
        # Push Submit button
        form_page.submit_form()

        #Summary tests
        assert form_page.header == "Thanks for submitting the form", "Header text is incorrect"
        assert form_page.name == self.name + " " + self.last_name, "Name or Last name is incorrect"
        assert form_page.email == self.mail, "E-mail address is incorrect"
        assert form_page.gender == self.gender, "Gender is incorrect"
        assert form_page.mobile_number == self.phone_number, "Phone number is incorrect"
        assert form_page.subject == self.subject, "Subject is incorrect"
        assert form_page.hobbies == self.hobbies, "Hobbies are incorrect"
        assert form_page.address == self.adress, "Address is incorrect"
        assert form_page.state_and_city == self.state_and_city, "State or City is incorrect"

        # Close summary
        form_page.close_summary()

