from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:

    driver.get("https://v1.training-support.net/selenium/login-form")

    print(driver.title)

    driver.find_element(By.ID, "username").send_keys("admin")

    driver.find_element(By.ID, "password").send_keys("password")

    driver.find_element(By.CSS_SELECTOR, ".ui.button").click()

    print(driver.title)

    driver.quit()

