from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import datetime

driver = webdriver.Chrome()

count_of_cryptos = 8

crypto_ID = {78:"BTC",7841:"ETH",6746:"USDT",8665:"SOL",2649:"BNB",80:"XRP",6739:"USDC",3498:"DOGE"}

while(1):
    price_list = {"BTC":0,"ETH":0,"USDT":0,"SOL":0,"BNB":0,"XRP":0,"USDC":0,"DOGE":0}
    for i in range(count_of_cryptos):
        driver.get(f"https://fcsapi.com/api-v3/crypto/latest?id={list(crypto_ID.keys())[i]}&access_key=8CNLQ22cKi2m2Evhq96xs")
        pre_element = driver.find_element(By.XPATH,"//pre")
        
        pre_text = pre_element.text
        pre_text = pre_text.split('"c":"')
        pre_text.pop(0)
        raw_price = ""
        for j in pre_text[0]:
            if j == '"':
                break
            else:
                raw_price += j

        price_list[list(price_list.keys())[i]] = float(raw_price)
        sleep(21)
    print("\n")
    current_time = datetime.datetime.now()
    print("time : ", current_time)
    for i in range(count_of_cryptos):
        print(f"{list(price_list.keys())[i]} : {list(price_list.values())[i]}")
