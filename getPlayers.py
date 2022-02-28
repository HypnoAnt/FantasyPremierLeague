from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#from bs4 import BeautifulSoup
#import requests

statsUrl = "https://fantasy.premierleague.com/statistics"
web = webdriver.Chrome()


def cookieDecline():
    web.get(statsUrl)
    time.sleep(3)
    cookieSettingsButton = web.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[5]/button[2]')
    cookieSettingsButton.click()
    cookieRejectButton = web.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[3]/div[1]/button[2]')
    cookieRejectButton.click()
    cookieRejectButton = web.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div[2]/button')
    cookieRejectButton.click()

def setViewType(viewType):
    viewTypeFormLocation = Select(web.find_element_by_xpath('/html/body/main/div/div[2]/div/div[1]/form/div/div[1]/div/div/select'))
    viewTypeFormLocation.select_by_visible_text(viewType)
    
def sortBy(sortType):
    sortTypeFormLocation = Select(web.find_element_by_xpath('/html/body/main/div/div[2]/div/div[1]/form/div/div[2]/div/div/select'))
    sortTypeFormLocation.select_by_visible_text(sortType)

cookieDecline()
time.sleep(1)
setViewType("Defenders")
sortBy("Team selected by %")


#stats_html = requests.get(statsUrl).text
#soup = BeautifulSoup(stats_html, 'lxml')
#players = soup.find_all('li',class_ = 'ElementTable__ElementRow-sc-1v08od9-3 kGMjuJ')
#print(players)
