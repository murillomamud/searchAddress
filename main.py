#%%
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#%%
## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
webdriver_service = Service("./src/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#%%
# Get page
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php?t")

#%%
elemen_cep = driver.find_element(By.NAME, 'endereco')
elemen_cmb = driver.find_element(By.NAME, 'tipoCEP')
elemen_button_search = driver.find_element(By.NAME, 'btn_pesquisar')
#%%
elemen_cep.clear()

#%%
elemen_cep.send_keys('09210760')
elemen_cmb.click()
driver.find_element(By.XPATH, '//*[@id="formulario"]/div[2]/div/div[2]/select/option[6]')

#%%
elemen_button_search.click()
time.sleep(10)

#%%
elemen_address = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')

#%%
street = elemen_address.get_attribute('innerHTML')
print(street)
#%%
elemen_cep.get_attribute('value')
# %%
driver.quit()