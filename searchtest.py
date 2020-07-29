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
        search_field = self.driver.find_elements_by_name("q")


    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_elements_by_class_name("input-test")

    def test_search_button_enabled(self):
        button = self.driver.find_elements_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_elements_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3,len(banners))

    def test_vip_promo(self):
        pass
        #vip_promo = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_elements_by_css_selector("div.header-minicart spam.icon")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    
    unittest.main(verbosity=2)

    