import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  #Exepción para validar la presencia de un elemento
from selenium.webdriver.common.by import By #Llamado de excepciones a validar 



class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")


    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,"q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID,"select-language"))
    
    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException:
            return False
        return True