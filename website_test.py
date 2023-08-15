import unittest
from selenium import webdriver

class WebsiteTest(unittest.TestCase):
    def setUp(self):
        # Create a new Chrome browser instance in headless mode
        print("Initializing Chrome browser...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(options=chrome_options)
        print("Chrome browser initialized.")

    def test_website_loading(self):
        print("Starting website loading test...")
        # Navigate to the atg.world website
        print("Navigating to atg.world website...")
        self.driver.get("https://atg.world")
        print("Website loaded.")

        # Check if the website title contains the expected text
        expected_title = "Across The Globe (ATG) - Professional and Personal Social Networking"
        print("Verifying website title...")
        if expected_title in self.driver.title:
            print("Website title is as expected.")
        else:
            self.fail("Website title is not as expected.")

    def tearDown(self):
        print("Cleaning up and closing the browser...")
        # Close the browser after the test
        self.driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    print("Running the test suite...")
    unittest.main()
