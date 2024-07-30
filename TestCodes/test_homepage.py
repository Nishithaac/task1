
# Page Object Model (POM)
#
# Page Object Model is a design pattern for writing clean and well-tested code.
# Every page of your web-application is now an Object
# POM is a set of classes which is designed to represent one or more web pages.
# Through POM we represents the element of a web page as an object
# It helps us write a code which is simple and easy to understand
# It gives us the power to keep all your automation testing codes well structured and easy to understand
#
# Advantages of POM
#
# Quality
# POM helps you to write automation testing code which is easy to understand and easy to maintain.
# It makes your code more easy to read and reliable
#
#
# Maintenance
# We can maintain our automation testing code easily
# If there are changes that we need to have we just need to change that Python file class only.
#
#
# Productivity
# Since the code is easy to maintain we have to write less code and we can make our code more efficient and reusable in other projects.
#
#
#
#
# Collaboration
# Since it is POM we can easily collaborate with fellow testers who can change the code as they want to do.
#
#
# Reusability
# Since, with POM we can reuse our classes, methods into different projects it helps us to write less code and be smart testers.

# Higher-order-function: a function that uses another function is called higher order function
import pytest

from TestData.HomepageData import Homepage
from TestLocators.HomepageLocators import Locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Test_Suman:
    @pytest.fixture
    # Booting function for running all the Python tests
    def booting_function(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield
        self.driver.close()
    def test_get_title(self,booting_function):
        self.driver.get(Homepage().url)
        assert self.driver.title==Homepage().title
        print("SUCCESS: Web page title is verified")

    def test_verify_url(self,booting_function):
        self.driver.get(Homepage().url)
        assert self.driver.current_url==Homepage().url
        print("SUCCESS: Homepage URL verified")
    def test_login(self,booting_function):
        try:
            self.driver.get(Homepage().url)
            self.driver.find_element(by=By.NAME, value=Locators().username_input_box).send_keys(Homepage().username)
            self.driver.find_element(by=By.NAME, value=Locators().password_input_box).send_keys(Homepage().password)
            self.driver.find_element(by=By.XPATH, value=Locators().submit_button).click()
            assert self.driver.current_url == Homepage().dashboard_url
            print("SUCCESS : Logged in with username {a} and password{b}".format(a=Homepage().username,
                                                                                 b=Homepage().password))
            # print(f"SUCCESS: Logged in with username {Homepage().username} and password {Homepage().password}")
        except NoSuchElementException as e:
            print(e)


