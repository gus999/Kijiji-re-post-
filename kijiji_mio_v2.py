from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import datetime
from time import sleep
from openpyxl import load_workbook
from openpyxl import Workbook
import os

'''
class kijiji (): 
'''

a = datetime.datetime.now()
print (a)
#create new Excel Workbook
wbWrite=Workbook()
options = Options()

options.add_argument("--start-maximized")
#Create webdriver on chromedriver from folder
######browser=webdriver.chromedriver (options=options)
#browser = webdriver.Chrome (options=options)
#options.add_argument('--headless')
browser = webdriver.Firefox (executable_path='./geckodriver', options=options)



browser.get('https://www.kijiji.ca/t-login.html')
#browser.get('https://www.google.com/')
sleep (2)


def login(usname, passw):
    
    browser.find_element_by_xpath ('//*[@id="LoginEmailOrNickname"]').send_keys(usname)
    browser.find_element_by_xpath('//*[@id="login-password"]').send_keys(passw)
    browser.find_element_by_xpath("//*[@id='SignInButton']").click()
login ("XXXXX", "XXXXX")
''' 
add options to browser
- 1) headless, usefull when script is complety funtional and validated.
- 2) start maximized
'''
sleep (120)   

#browser.switch_to_active_element ()
#browser.find_element_by_class_name("link-2454463992").click



# My Profile
browser.find_element_by_class_name ("root-150276580").click ()
# Open my Ads
browser.find_element_by_class_name ("listItem-3079336677").click ()

sleep (9)
#Edit my add
browser.find_element_by_class_name ("buttonText-3081832346").click()
#LOOP FOR WHILE TRUE
sleep (10)
#Add Price
price=browser.find_element_by_xpath ("//*[@id='PriceAmount']")
price.clear()
price.send_keys (99)

browser.find_element_by_name ("saveAndCheckout").click()

#Loop begins here



# loop will continue for 10 hours, updating every 5 min.
for y in range (120):
    browser.find_element_by_class_name ("edit-ad-begin").click()
    sleep (6)
    pricey=browser.find_element_by_xpath ("//*[@id='PriceAmount']").get_attribute ("value")
    if pricey==str (99):
        price=browser.find_element_by_xpath ("//*[@id='PriceAmount']")
        price.clear()
        price.send_keys (98)
        print (str (pricey) + " in if-1")
    else:
        price=browser.find_element_by_xpath ("//*[@id='PriceAmount']")
        price.clear()
        price.send_keys (99)
        print (str (pricey) + " in if-2")
    browser.find_element_by_name ("saveAndCheckout").click()
    print ("contador  =" + str (y))
    sleep (300)
#browser.find_element_by_class_name ("edit-ad-begin").click()
    #counter+=1
    
    

         
b = datetime.datetime.now()
print (b)
c = (b - a)





