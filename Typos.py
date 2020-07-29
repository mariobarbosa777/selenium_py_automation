import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


from time import sleep


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[43]/a').click()
 
    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1 
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
            text_to_check = paragraph_to_check.text
            tries += 1
            driver.refresh()

        found=True

        self.assertEqual(found,True)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main( verbosity= 2, testRunner= HTMLTestRunner( output = "reportes", report_name="Typos"))