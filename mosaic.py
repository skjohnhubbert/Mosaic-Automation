##loads mosaic on firefox
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


fp = webdriver.FirefoxProfile('C:/Users/sahubbert/AppData/Roaming/Mozilla/Firefox/Profiles/ylwc54e4.dev-edition-default')
driver = webdriver.Firefox(fp)
driver.get('https://heartlandmosaic.com/sf01346307Mosaic')

## mosaic log in
login = driver.find_element_by_id('UserName')
login.send_keys('sahubbert')
passwordElem = driver.find_element_by_id('Password')
passwordElem.send_keys('4731')
passwordElem.submit()

time.sleep(3)

reports = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[3]/a')
reports.click()

sales = driver.find_element_by_xpath('//*[@id="page"]/div/div/table/tbody/tr[2]/td[1]/a[2]/div')
type(driver)
sales.click()

daily_sales_report = driver.find_element_by_xpath('//*[@id="ReportsMenu"]/div/div/table/tbody/tr[2]/td[1]/a[11]/div')
type(driver)
daily_sales_report.click()

down_arrow = driver.find_element_by_xpath('//*[@id="fields"]/table/tbody/tr[1]/td[2]/span/span/span[2]/span')
type(down_arrow)
down_arrow.click()

time.sleep(3)
gradus = driver.find_element_by_xpath('//*[@id="35ae43c8-ef13-412a-9b8b-e2576c0cd34a"]')
ActionChains(driver).move_to_element(gradus)
gradus.click()


