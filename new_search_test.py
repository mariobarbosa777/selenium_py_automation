import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    def test_search_tee(self):
        driver = self.driver
        search_filed = driver.find_element_by_name("q")
        search_filed.clear()

        search_filed.send_keys("tee")
        search_filed.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_filed = driver.find_element_by_name("q")
        search_filed.clear()

        search_filed.send_keys("salt shaker")
        search_filed.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()

