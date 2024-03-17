from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
while(1):
    
    driver.get("https://fcsapi.com/api-v3/crypto/latest?id=78,7841,6746,8665,2649,80,6739,3498&access_key=8CNLQ22cKi2m2Evhq96xs")
    #78->BTC/USD
    #7841->ETH/USD
    #6746->USDT/USD
    #8665->SOL/USD
    #2649->BNB/USD
    #80->XRP/USD
    #6739->USDC/USD
    #3498->DOGE/USD

    pre_element = driver.find_element(By.XPATH,"//pre")

    pre_text = pre_element.text
    pre_text = pre_text.split('"c"')
    pre_text.pop(0)

    price_list = {"BTC":0,"ETH":0,"USDT":0,"SOL":0,"BNB":0,"XRP":0,"USDC":0,"DOGE":0}

    for i in range(8):
        raw_price = ""
        counter = 0
        for j in pre_text[i]:
            if j == ":" or j == '"':
                counter += 1
            else:
                raw_price += j
            
            if counter > 2:
                break

        price_list[list(price_list.keys())[i]] = float(raw_price)

    for i in range(8):
        print(f"{list(price_list.keys())[i]} : {list(price_list.values())[i]}")

    sleep(300)
    os.system('cls')
    