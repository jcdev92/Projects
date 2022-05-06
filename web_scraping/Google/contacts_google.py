import time
from selenium import webdriver

drive = webdriver.Chrome(executable_path="/home/gordo/jmcg_dev/Projects/web_scraping/Google/chromedriver_linux64/chromedriver")

time.sleep(5)
drive.quit()