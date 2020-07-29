import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")


    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("platzi")
        search_field.submit()

        driver.back()
        driver.forward()
        driver.refresh()
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main( verbosity= 2, testRunner= HTMLTestRunner( output = "reportes", report_name="automatic-Navigation"))