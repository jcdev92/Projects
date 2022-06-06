from selenium import webdriver
import time
import os

web = "https://twitter.com/i/flow/login"
path = "/Users/frankandrade/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# espera de 6 segundos para dejar que la pagina cargue el contenido
time.sleep(6)  # los segundos pueden varias segun tu computadora

# localizar los inputs username y password. Luego enviar texto a los inputs
# username
username = driver.find_element_by_xpath('//input[@autocomplete ="username"]')
username.send_keys("my_username")  # Escribir email/usuario aqui
# username.send_keys(os.environ.get("TWITTER_USER"))

# Click en boton "Next"
next_button = driver.find_element_by_xpath('//div[@role="button"]//span[text()="Next"]')
next_button.click()

# espera de 2 segundos luego de hacer click en boton
time.sleep(2)

# password
password = driver.find_element_by_xpath('//input[@autocomplete ="current-password"]')
password.send_keys("my_password")  # Escribir password aqui
# password.send_keys(os.environ.get("TWITTER_PASS"))

# localizar boton de login y luego hacer click
login_button = driver.find_element_by_xpath('//div[@role="button"]//span[text()="Log in"]')
login_button.click()

# cerrar driver
# driver.quit()
