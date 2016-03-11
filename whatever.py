import os
from selenium import webdriver
import time
query = raw_input("What do you wanna search for?").split(' ')

q="https://www.youtube.com/results?search_query="

for i in range(0,len(query)):
	q=q+query[i]+'+'
print q
os.system('cls')
driver = webdriver.PhantomJS('D:/Py/phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.maximize_window()
driver.get(q)
print "\nOpened up the webpage!"
time.sleep(4)
elem = driver.find_element_by_class_name('yt-lockup-title')
elem.click()
print "\nGot the song you wanted!"
time.sleep(3)
curr =  driver.current_url
print "\nGot the URL!"
driver.close()
print "\nClosed the WebDriver!"


os.system('youtube-dl --extract-audio --audio-format mp3 %s' % curr)
print "\nDone"