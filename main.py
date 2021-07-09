from selenium import webdriver
import requests
from csv import writer
from bs4 import BeautifulSoup as bs
browser = webdriver.Firefox(
    executable_path=r'/home/carebear/Desktop/Work/VENV/geckodriver')
browser.get('http://3.7.89.203/login/index.php')
browser.find_element_by_id('username').send_keys('archmaze')
browser.find_element_by_id('password').send_keys('1U@zzzzzz')
browser.find_element_by_id('loginbtn').click()
ind = 1
for serial in range(29010, 29491):
    try:
        uri = "http://3.7.89.203/user/profile.php?id={}".format(serial)
        browser.get(uri)
        name_raw = browser.find_element_by_class_name('page-header-headings')
        elements = browser.find_element_by_class_name('userprofile')
        email = ''
        country = ''
        mob = ''
        clg = ''
        city = ''
        name = name_raw.text
        sampleText = elements.text
        for item, next_item in zip(sampleText.split(), sampleText.split()[1:]):
            if item == 'Country':
                country = next_item
            if item == 'City/town':
                city = next_item
            if item == 'address':
                email = next_item
            if item == 'Mobile':
                mob = next_item
            if item == 'Name':
                clg = next_item

        lst = [ind, name, country, city, email, mob, clg]
        ind+=1
        with open('strum.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(lst)
    except:
        pass

f_object.close()
