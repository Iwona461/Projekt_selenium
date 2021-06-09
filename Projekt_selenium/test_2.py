import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

invalid_login = "Iwona"
valid_password = "Reggaeton2021"

class Allegro_sign_in(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_sign_in_allegro(self):
        driver = self.driver
        driver.get("https://allegro.pl/") # navigate to a page given by the URL
        self.assertIn("allegro", driver.title) # The next line is an assertion to confirm that title has “Python” word in it
        zaloguj_btn = driver.find_element_by_link_text("Zalogujsie")
        zaloguj_btn.click()
        logoption_btn = driver.find_element_by_id("emailCredentialsSwitch")
        logoption_btn.click()
        login_field = driver.find_element_by_name("login")
        login_field.click()
        input_login = driver.find_element_by_xpath("//input[@placeholder='Login lub e-mail']")
        input_login.send_keys(invalid_login)
        haslo_field = driver.find_element_by_xpath("//input[@placeholder='Hasło']")
        haslo_field.send_keys(valid_password)
        zaloguj1_btn = driver.find_element_by_type("submit")
        zaloguj1_btn.click()
        error_notice = driver.fint_element_by_id("login-form-submit-error")
        print(error_notice.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":  # uruchomienie zestawu testowego
    unittest.main()
