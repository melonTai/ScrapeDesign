import unittest
from selenium import webdriver
from mypackage import page
import time

class DesignPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://iterograph.laboiteatortue.com/#/")

    def test_generate_design(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "itereograph title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.set_layer()
        main_page.download_image()
        time.sleep(2)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()