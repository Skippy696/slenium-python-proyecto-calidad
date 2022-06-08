
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def set_up():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    driver.maximize_window()
    return driver

def test_google(driver):
    driver.get('https://www.google.com/')
    driver.find_element(By.NAME, 'q').send_keys('Selenium')
    driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
    driver.close()
    driver.quit()

    # main method
if __name__ == '__main__':
    driver = set_up()
    test_google(driver)
    print('Test completed')