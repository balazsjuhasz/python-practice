from selenium import webdriver

PATH = "/home/balazs/chrome-driver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")