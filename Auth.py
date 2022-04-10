from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from imgurpython import  ImgurClient
import configparser
# the information of the client account:

def authenticate():
    config = configparser.ConfigParser()
    config.read('information')

    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    client_username = config.get('credentials', 'imgur_username')
    client_password = config.get('credentials', 'imgur_password')

    # objectify the client
    client = ImgurClient(client_id=client_id, client_secret=client_secret)

    authorization_url = client.get_auth_url('pin')

    driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver.get(authorization_url)

    #Objectify the Check box to minplute it inside python , through find element by xpath wich the id in html
    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')

    #send a value to the check box
    username.send_keys(client_username)
    password.send_keys(client_password)

    #calling for a botton by it's name in html and use the mothed click() to click it
    driver.find_element_by_name("allow").click()

    #save guard to make sure the page load before we insert the information
    timeout = 5
    try:
        #checking to see if that element that you want is exsit in the page by it's ID
        element_present = EC.presence_of_element_located((By.ID,"pin"))

        #a mothed makes the browser to wait untill the element we wating for is presence
        WebDriverWait(driver,timeout).until(element_present)
        # find  the element to store it by its ID html
        pin_element = driver.find_element_by_id('pin')
        # get the element value
        pin = pin_element.get_attribute("value")
    except TimeoutException:
        print('Timed out wating for page load')
    driver.close()

    #a function the filed the pin
    credentials = client.authorize(pin,'pin')
    client.set_user_auth(credentials['access_token'],credentials['refresh_token'])
    print("authentication successful")

    return client

# # gallery is a mothed that bring all the front page items
# itmes = client.gallery()
#
#
#
#
#
# for itme in itmes:
#     print(itme.link)
#     print(itme.views)
#     print(itme.title)
#
# #find the image on the front page that has the highest number of views
#
# max_item = None
# max_views = 0
# for item in itmes:
#     if item.views > max_views:
#         max_views = item.views
#         max_item = item
#
# print('Max Vies is: ',max_views)
# print('the title of the item is: ', max_item.title)
