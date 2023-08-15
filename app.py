import unittest
from selenium import webdriver

class TestATGWorldWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # You can use a different browser driver
        self.url = "https://atg.world"

    def test_website_loading(self):
        self.driver.get(self.url)
        title = self.driver.title
        self.assertNotEqual(title, "Error")  # You can customize this check

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

