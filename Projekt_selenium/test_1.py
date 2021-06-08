import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(pytest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org") # navigate to a page given by the URL
        self.assertIn("Python", driver.title) # The next line is an assertion to confirm that title has “Python” word in it
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":  # uruchomienie zestawu testowego
    unittest.main()
