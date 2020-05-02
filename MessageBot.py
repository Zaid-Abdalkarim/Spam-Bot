import requests
import json 
import selenium
import time
from selenium import webdriver
from pynput.mouse import Button, Controller
from lyrics_api import *

i = 1

driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/bin/chromedriver.exe')
driver.get('http://web.airdroid.com/')

pass_box = driver.find_element_by_class_name("widget-login-account-input")
pass_box.send_keys('your own email')


pass_box = driver.find_element_by_class_name('widget-login-pwd-input')
pass_box.send_keys('Your own password')
pass_box.send_keys(u'\ue007')

time.sleep(0.5)

confirm_button = driver.find_element_by_class_name("select-device-item.active")
confirm_button.click()

time.sleep(1)

messages_button = driver.find_element_by_id("icon_1_0_136840")
messages_button.click()

time.sleep(1.5)

message_sender = driver.find_element_by_xpath("//div[@aria-label='input message']")
message_sender.send_keys('yooooo') #this is a test message you dont need this
message_sender.send_keys(u'\ue007')




track_name = "Blinding Lights"
artist_name = ""

api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
request = requests.get(api_call)
data = request.json()
data = data['message']['body']
anwar = data['lyrics']['lyrics_body']
lyrics = json.dumps(anwar)
lyrics.replace('\n', ' ')
while(lyrics != " "):
    word = lyrics
    inte = word.index(' ')
    word = word[0: inte]
    lyrics = lyrics[inte + 1 : ]
    message_sender.send_keys(word)
    message_sender.send_keys(u'\ue007')
    #await ctx.send(word)
print(data['lyrics']['lyrics_body'])