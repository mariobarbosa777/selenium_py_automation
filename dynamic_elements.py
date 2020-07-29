import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep


class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[9]/a').click()
 
    def test_name_elements(self):
        driver = self.driver

        len_menu = 5
        tries = 0
        menu = []

        while len(menu) < len_menu:
            tries += 1
            menu = driver.find_elements_by_xpath('//*[@id="content"]/div/ul/li')
            driver.refresh()

        print(f"number of tries: {tries}")



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main( verbosity= 2, testRunner= HTMLTestRunner( output = "reportes", report_name="dynamic-elements"))