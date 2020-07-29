import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class DynamicControl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[13]/a').click()
 
    def test_dynamic_controls(self):
        driver = self.driver
        
        driver.find_element_by_xpath('//*[@id="checkbox-example"]/button').click()

        add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
        add_button.click()

        remove_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))

        checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkbox"]')))
        checkbox.click()
        sleep(1)
        checkbox.click()
        sleep(1)


        enabled_button = driver.find_element_by_xpath('//*[@id="input-example"]/button')
        enabled_button.click()
    
        textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input')))
        textbox.send_keys("Hola Mundo!!")
        sleep(1)

        enabled_button.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
        enabled_button.click()

        textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input')))
        textbox.clear()
        textbox.send_keys("Adios Mundo!!")
        sleep(1)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main( verbosity= 2, testRunner= HTMLTestRunner( output = "reportes", report_name="dynamic-elements"))