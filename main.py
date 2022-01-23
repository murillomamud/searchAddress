#%%
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import json

#%%
cep = sys.argv[1]

if not cep:
    cep = '09210760'
    
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
elemen_cep.send_keys(cep)
elemen_cmb.click()
driver.find_element(By.XPATH, '//*[@id="formulario"]/div[2]/div/div[2]/select/option[6]')

#%%
elemen_button_search.click()
time.sleep(1)

#%%
street = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').get_attribute('innerHTML')
#
district = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').get_attribute('innerHTML')

city = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').get_attribute('innerHTML')
#%%
print("""
ZipCode: {} 
Street: {}
District: {}
City: {}

""".format(cep,street,district,city))

data = {"zipCode":cep, "street":street, "district":district, "city":city}
ret = json.dumps(data)
print(ret)

#%%
elemen_cep.get_attribute('value')
# %%
driver.quit()