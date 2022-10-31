from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

FlooderNumber=str(1)
FlooderDurchgang=int(input("Schreibe wie viele Bots du haben willst\n"))
Durchgegangen=int(1)
KahootCode=input("Schreibe den Code von dem Kahoot.\n")
FlooderName=input("Schreibe wie die Bots heissen sollen.\n")

while Durchgegangen<=FlooderDurchgang:
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://kahoot.it")
    print(driver.title)

    search = driver.find_element(By.ID, "game-input")
    search.send_keys(KahootCode)
    search.send_keys(Keys.RETURN)

    time.sleep(0.5)

    search = driver.find_element(By.ID, "nickname")
    search.send_keys(FlooderName, FlooderNumber)
    search.send_keys(Keys.RETURN)

    time.sleep(0.5)

    #driver.quit()
    Durchgegangen=Durchgegangen+1
    FlooderNumber=int(FlooderNumber)
    FlooderNumber=int(FlooderNumber)+1
    FlooderNumber=str(FlooderNumber)
    print(Durchgegangen)
    print(FlooderDurchgang)