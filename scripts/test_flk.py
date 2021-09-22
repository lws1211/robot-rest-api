#!/usr/bin/env python3
import requests, time
# import webbrowser
# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get("http://127.0.0.1:7201/api/robot/status")
while True:
    response = requests.get("http://127.0.0.1:7201/api/robot/status")
    if response.status_code == 200:
        print(response.json()) 
    elif response.status_code == 400:
        print(response.status_code, "bad request", end="\t")
        print(response.json()) 
    # driver.refresh( )
    #webbrowser.open("http://127.0.0.1:7201/api/robot/status", new=0, autoraise=True)
    
    time.sleep(1)