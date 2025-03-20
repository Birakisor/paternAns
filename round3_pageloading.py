from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= option)
URL = "https://mathup.com/games/crossbit?mode=championship"


totalTime = 0
for i in range(10):
    startTime = time.time()
    
    driver.get(URL)
    time.sleep(3)
    loadTime = time.time() - startTime
    totalTime+= loadTime

print(totalTime)

print(f" Average time : {totalTime/10}")
