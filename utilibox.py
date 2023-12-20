from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import os

class Toolbox:
    load_dotenv()
    secret_username = os.getenv('USERNAME1')
    secret_password = os.getenv('PASSWORD1')
    secret_username1 = os.getenv('INVALID_USERNAME')
    secret_password1 = os.getenv('INVALID_PASSWORD')


    def url(self):
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
        page_url = self.driver.current_url
        assert os.getenv('BASE_URL') in page_url


    def login(self,username,password): 
        self.driver.find_element(By.CSS_SELECTOR, '#signin_button').click() 
        self.driver.find_element(By.CSS_SELECTOR, "#user_login").send_keys(username) 
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys(password) 
        self.driver.find_element(By.CSS_SELECTOR, '#user_remember_me').click() 
        self.driver.find_element(By.CSS_SELECTOR, 'input[value="Sign in"]').click() 