from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= options)

# Already take championship link here
URL = "https://mathup.com/games/crossbit?mode=championship"


for i in range(10):
    driver.get(URL)
    time.sleep(6)

    Start_elements = driver.find_element(By.XPATH,'//div[@class="GamePostStart_btn__yoMra btn "]')
    Start_elements.click()
        
    element = driver.find_elements(By.XPATH,"//div[@class='GamePostStart_value__zH0b9']")

    print(f" Defuculty : {element[1].text}")

