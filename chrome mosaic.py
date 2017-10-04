from selenium import webdriver
from datetime import datetime, timedelta, date
from time import strftime

driver = webdriver.Chrome(executable_path=r"C:\Python34\chrome\chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get('https://heartlandmosaic.com/sf01346307Mosaic');

#log in
login = driver.find_element_by_id('UserName')
login.send_keys('sahubbert')
passwordElem = driver.find_element_by_id('Password')
passwordElem.send_keys('4731')
passwordElem.submit()

#reports
reports = driver.find_element_by_xpath('//*[@id="Reports"]/a')
type(driver)
reports.click()

#report type sales
sales = driver.find_element_by_xpath('//*[@id="page"]/div/div/table/tbody/tr[2]/td[1]/a[2]/div')
type(driver)
sales.click()

#daily sales report
daily_sales_report = driver.find_element_by_xpath('//*[@id="ReportsMenu"]/div/div/table/tbody/tr[2]/td[1]/a[11]/div')
type(driver)
daily_sales_report.click()

today = datetime.today()
start_date = today.replace(day=8, month=8, year=2017)

send_date = driver.find_element_by_id('StartDate')
send_date.send_keys()

while True:
    if today > start_date:
        today = today - timedelta(days = 1)
        today_strftime = today.strftime('%m/%d/%Y')
        send_date = driver.find_element_by_id('StartDate')
        send_date.send_keys(today.strftime)
        display = driver.find_element_by_id('btnDisplayReport')
        print(today_strftime)
    if today == start_date:
        break

#down arrow
down_arrow = driver.find_element_by_xpath('//*[@id="fields"]/table/tbody/tr[1]/td[2]/span/span/span[2]/span')
type(down_arrow)
down_arrow.click()

gradus = driver.find_element_by_css_selector('#SchoolGroupId_listbox > li:nth-child(17)')
type(gradus)
gradus.click()

