from selenium.webdriver.common.by import By
import time
import os
from utilibox import Toolbox
from selenium.webdriver import Keys

class Testlandingpage(Toolbox):

    def test_landing_page(self):
        self.url()
        landing_page_text = self.driver.find_element(By.CSS_SELECTOR, '.brand').text
        print(landing_page_text)

        assert landing_page_text == 'Zero Bank'


    def test_searchbox(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, '#searchTerm')
        search_box.send_keys('faketest')
        search_box.send_keys(Keys.ENTER)
        assert self.driver.find_element(By.CSS_SELECTOR, '.top_offset > h2').text == 'Search Results:'

