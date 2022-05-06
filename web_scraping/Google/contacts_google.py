import time
from selenium import webdriver

drive = webdriver.Chrome(executable_path="Ubuntu\home\gordo\jmcg_dev\Projects\web_scraping\Google\chromedriver")

time.sleep(5)
drive.quit()