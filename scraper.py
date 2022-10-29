from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

####################Scraping data######################

#Initializing the driver and getting the page
driver = webdriver.Edge()
driver.get('https://www.losmundialesdefutbol.com/estadisticas/tabla_de_posiciones.php')
driver.maximize_window()

#Finding elements
driver.implicitly_wait(5)
countries = driver.find_elements(By.CLASS_NAME, 'a-top.bb-2')
headers = driver.find_element(By.CLASS_NAME, 't-enc-5.a-right.a-bottom')
headers = headers.text.split(' ')

#################Cleaning a little bit the data so we can write it to a csv file properly#####################

countries_lst = []
won_cups_lst = []

#Get number of cups won by country (We have to do this because the page shows imgs of the cup and not the number)
for country in countries:
    cups = country.find_elements(By.TAG_NAME, 'img')
    won_cups = len(cups) - 1
    country_lst = country.text.split(' ')
    countries_lst.append(country_lst)
    won_cups_lst.append(won_cups)

#Adds number of cups won to each country
i = 0
for c in countries_lst:
    if len(c) == 11:
        c.insert(3, won_cups_lst[i])
        i += 1

#Fixes error (some countries have more then one word so that row has more elements ex: Corea,del,Sur -----> Corea del Sur)
for i in countries_lst:
    if len(i) == 13:
        i[1] += ' ' + i[2]
        i.pop(2)
    elif len(i) == 14:
        i[1] += ' ' + i[2] + ' ' + i[3]
        i.pop(2)
        i.pop(2)

#Fixes the rare thigs in the header
headers[0] = headers[0].split('\n')
headers = headers[0] + headers[1:]
headers.pop()
headers.pop()

#Write data to csv file
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for country in countries_lst:
        writer.writerow(country)

#Closing driver
driver.close()
