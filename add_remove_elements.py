import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a').click()
 
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input("How many would you add ?: "))
        elements_removed = int(input("How many would you detele ?: "))

        total_elements = elements_added - elements_removed

        add_button =  driver.find_element_by_xpath('//*[@id="content"]/div/button')

        for i in  range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                driver.find_element_by_xpath('//*[@id="elements"]/button[1]').click()
            except:
                print("No more buttons to delete")
                break

        if total_elements >0:
            print(f"There are {total_elements}")
        else: 
            print(f"There are no elements")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main( verbosity= 2, testRunner= HTMLTestRunner( output = "reportes", report_name="add-delete"))