import unittest
from pyunitreport import HTMLTestRunner 
from selenium import webdriver 

class HelloWorld(unittest, TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"chromedriver.exe"
        driver = self.driver.
    
    
    def test_hello_world(self):
        pass


    def tearDown(self):
        retunr super().tearDown()
    
if __name__ == "__main__":
    unittest.main( verbosity= 2, testRunner= HTMLTestRunner( output = "reportes", report_name)