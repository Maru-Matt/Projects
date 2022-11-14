import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3206109275&geoId=101630962&keywords=python%20developer&location=Virginia%2C%20United%20States&refresh=true"
chrome_driver_path = "/Users/matiyasmaru/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "nav__button-secondary").click()
driver.find_element(By.ID, "username").send_keys("matiyasmaru@gmail.com")
driver.find_element(By.ID, "password").send_keys("y8#h0*O1+s1)")
driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
time.sleep(5)

number_to_jobs_to_apply = 20
while number_to_jobs_to_apply > 0:
    try:
        # Easy apply filter
        driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[8]/div').click()
        time.sleep(2)
        # Autofill phone number
        apply = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div')
        apply.click()
        time.sleep(2)
        # Resume attach
        driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary').click()
        time.sleep(2)
        # submit
        driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary').click()
        time.sleep(2)
        # driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary').click()
        # driver.find_element(By.CSS_SELECTOR, '.artdeco-button--primary').click()
        number_to_jobs_to_apply -= 1
    except selenium.common.exceptions.ElementNotInteractableException:

        continue

