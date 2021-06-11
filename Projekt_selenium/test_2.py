import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.Chrom.options import Options
import time

invalid_login = "Iwona"
valid_password = "Reggaeton2021"

class Allegro_sign_in(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_sign_in_allegro(self):
        driver = self.driver
        driver.get("https://allegro.pl/") # navigate to a page given by the URL
        self.assertIn("Allegro", driver.title) # The next line is an assertion to confirm that title has “Python” word in it
        zgoda_btn = driver.find_element_by_link_text("Ok, zgadzam się")
        zgoda_btn.click()
        time.sleep(10)
        zaloguj_btn = driver.find_element_by_link_text("zaloguj się")
        zaloguj_btn.click()
        time.sleep(10)
        logoption_btn = driver.find_element_by_id("emailCredentialsSwitch")
        logoption_btn.click()
        login_field = driver.find_element_by_name("login")
        login_field.click()
        input_login = driver.find_element_by_xpath("//input[@placeholder='Login lub e-mail']")
        input_login.send_keys(invalid_login)
        time.sleep(5)
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
