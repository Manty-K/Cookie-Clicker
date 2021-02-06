from selenium import webdriver
import time

driver_path = '/Users/SAM/Development/chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

url = 'https://orteil.dashnet.org/experiments/cookie/'

driver.get(url)

click_cookie = True
cookie = driver.find_element_by_id('cookie')


def getMoney():
    money = driver.find_element_by_id('money')
    money = money.text
    money = money.replace(',','')
    return int(money)


def getTimeMachinePrice():
    data = driver.find_element_by_id('buyTime machine')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[3]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)


def getPortalPrice():
    data = driver.find_element_by_id('buyPortal')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[2]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)


def getAlchemyLabPrice():
    data = driver.find_element_by_id('buyAlchemy lab')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[3]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)


def getShipmentPrice():
    data = driver.find_element_by_id('buyShipment')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[2]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)


def getMinePrice():
    data = driver.find_element_by_id('buyMine')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[2]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)


def getFactoryPrice():
    data = driver.find_element_by_id('buyFactory')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[2]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)


def getGrandmaPrice():
    data = driver.find_element_by_id('buyGrandma')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[2]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)

def getCursorPrice():
    data = driver.find_element_by_id('buyCursor')
    data_text = data.text
    split_text = data_text.split()
    amount_txt = split_text[2]
    amount_txt = amount_txt.replace(',', '')
    return int(amount_txt)

def buyProduct():
    money = getMoney()
    if money > getTimeMachinePrice():
        data = driver.find_element_by_id('buyTime machine')
        data.click()
    elif money > getPortalPrice():
        data = driver.find_element_by_id('buyPortal')
        data.click()
    elif money > getAlchemyLabPrice():
        data = driver.find_element_by_id('buyAlchemy lab')
        data.click()
    elif money > getShipmentPrice():
        data = driver.find_element_by_id('buyShipment')
        data.click()
    elif money > getMinePrice():
        data = driver.find_element_by_id('buyMine')
        data.click()
    elif money > getFactoryPrice():
        data = driver.find_element_by_id('buyFactory')
        data.click()
    elif money > getGrandmaPrice():
        data = driver.find_element_by_id('buyGrandma')
        data.click()
    elif money > getCursorPrice():
        data = driver.find_element_by_id('buyCursor')
        data.click()
while True:
    t_end = time.time() + 5
    while time.time() < t_end:
        cookie.click()
    buyProduct()