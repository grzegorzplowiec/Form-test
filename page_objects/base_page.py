from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str, str], text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple[str, str], time: int = 10):
        self._wait_until_element_to_be_clickable(locator, time)
        self._find(locator).click()

    def _autocompleteselect(self, locator: tuple[str, str], input_locator: tuple[str, str], text: str, time: int = 10):
        self._wait_until_element_to_be_clickable(locator, time)
        element = self._find(locator)
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self._click(locator, time)
        self._type(input_locator, text, time)
        self._type(input_locator, Keys.ARROW_DOWN, time)
        self._type(input_locator, Keys.ENTER, time)

    def _autoselect(self, locator: tuple[str, str], option: tuple[str, str], time: int = 10):
        self._wait_until_element_to_be_clickable(locator, time)
        element = self._find(locator)
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self._click(locator, time)
        self._click(option, time)


    def _wait_until_element_is_visible(self, locator: tuple[str, str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_to_be_clickable(self, locator: tuple[str, str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _wait_until_invisibility_of_element_located(self, locator: tuple[str, str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple[str, str], time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _get_value_of_css_property(self, locator: tuple[str, str], property: str, timeout: int = 10) -> str:
        self._wait_until_element_is_visible(locator, timeout)
        return self._find(locator).value_of_css_property(property)