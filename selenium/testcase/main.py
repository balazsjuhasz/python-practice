import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome(
            "/home/balazs/chrome-driver/chromedriver")
        self.driver.get("http://www.python.org")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()