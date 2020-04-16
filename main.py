import requests
from bs4 import BeautifulSoup
import config
import time
import smtplib
smtpObj = smtplib.SMTP('...', 587)
smtpObj.starttls()
smtpObj.login("...", "...")
def string_to_float(str):
    return float(str.replace(',', '.'))
def returning_value():
    full_page = requests.get(config.urlDollar, headers=config.headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb"})
    return string_to_float(convert[0].text)
def checking():
    firstValue = returning_value()
    time.sleep(0.5)
    secondValue = returning_value()
    if secondValue>firstValue:
        smtpObj.sendmail("...","...","Dollar povisilsia na "+str(secondValue-firstValue)+"||Seichas dollar stoit: "+str(secondValue))
        smtpObj.sendmail("...", "...","Dollar povisilsia na " + str(secondValue - firstValue) + "||Seichas dollar stoit: " + str(secondValue))
    if firstValue>secondValue:
        smtpObj.sendmail("...", "...","Dollar upal na " + str(firstValue-secondValue)+"||Seichas dollar stoit: "+str(secondValue))
        smtpObj.sendmail("...", "...","Dollar upal na " + str(firstValue - secondValue) + "||Seichas dollar stoit: " + str(secondValue))
    checking()
checking()