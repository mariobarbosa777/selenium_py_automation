import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(1)


    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")


    def test_search_text_field_by_name(self):
        search_field = self.driver.find_elements_by_name("input-test")


    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_elements_by_class_name("input-test")

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    
    unittest.main(verbosity=2)