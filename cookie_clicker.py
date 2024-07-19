from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep the browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create the driver
driver = webdriver.Chrome(options=chrome_options)
# Maximize the window
driver.maximize_window()
# Open the website
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie to click on
cookie = driver.find_element(By.ID, value="cookie")
# Find the right panel ids
right_panel = driver.find_elements(By.CSS_SELECTOR, value="#store div")
ids = [idA.get_attribute("id") for idA in right_panel]
# Count 5 minutes
duration = time.time() + 60 * 5
buy_time = time.time() + 10

game_on = True

while game_on:
    # Click the cookie
    for x in range(100):
        cookie.click()
    # Check every 5 seconds for upgrades
    if time.time() > buy_time:
        # Get the prices
        prices_upgrades = [i.text.split("-") for i in driver.find_elements(By.CSS_SELECTOR, value="#store b")]
        prices_upgrades.pop()
        prices = [int(price[1].strip().replace(",", "")) for price in prices_upgrades]
        # Get the money
        cookies = driver.find_element(By.ID, value="money").text
        if "," in cookies:
            cookies.replace(",", "")
        money = int(cookies)
        # Check the available purchases
        max_index = 0
        for i in range(len(prices)):
            if money >= prices[i]:
                max_index = i
        # Get the upgrade
        try:
            driver.find_element(By.ID, ids[max_index]).click()
        except ValueError:
            pass
        finally:
            buy_time = time.time() + 10

    if time.time() > duration:
        cps = driver.find_element(By.ID, value="cps").text
        print(cps)
        game_on = False

    money = int(driver.find_element(By.ID, value="money").text)
