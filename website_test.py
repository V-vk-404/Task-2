# test_website.py
import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):

    def test_website_connection(self):
        url = "https://atg.world"
        print(f"Testing website connection to {url}...")
        
        response = requests.get(url)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            print(f"Connected to {url} successfully. Status code: {response.status_code}")
        else:
            print(f"Failed to connect to {url}. Status code: {response.status_code}")
        
        # Assert the status code is 200
        self.assertEqual(response.status_code, 200, f"Test failed: Status code is not 200")

if __name__ == '__main__':
    unittest.main()
