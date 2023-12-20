
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver



@pytest.fixture(autouse=True, scope='class')
def setup(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver = WebDriver(options=options)
    request.cls.driver = driver

    yield 
    
    driver.implicitly_wait(15)
    driver.close()
    driver.quit()
