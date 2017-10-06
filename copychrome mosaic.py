from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta, date
from time import strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#date definitions
today = datetime.today()
start_date = today.replace(day=8, month=8, year=2017)

#form completion; StartDate/End Date ticker with form insertion
#display type selection, once report is displayed it will loop back, subtract 1 day from the current date and continue until start_date
keep_going = True
while keep_going:
    if today > start_date:
        today = today - timedelta(days=1)
        today_strftime = today.strftime('%m/%d/%Y')
        keep_going = False
        send_date = driver.find_element_by_id('StartDate')
        send_date.send_keys(today_strftime)
        send_date = driver.find_element_by_id('EndDate')
        send_date.send_keys(today_strftime)
        down_arrow = driver.find_element_by_xpath('//*[@id="fields"]/table/tbody/tr[7]/td[2]/span')
        down_arrow.click()
        excel = True
        while excel:
            if down_arrow == driver.find_element_by_xpath('//*[@id="fields"]/table/tbody/tr[7]/td[2]/span'):
                down_arrow.send_keys('e')
                down_arrow.click()
                excel = False
                display_button = True
                display = driver.find_element_by_xpath('//*[@id="btnDisplayReport"]')
                while display_button:
                    if display == driver.find_element_by_xpath('//*[@id="btnDisplayReport"]'):
                        display.click()
                        display_button = False
                        switch_tab = True
                        display = driver.find_element_by_xpath('//*[@id="btnDisplayReport"]')
                        while switch_tab:
                            if display == driver.find_element_by_xpath('//*[@id="btnDisplayReport"]'):
                                driver.switch_to.window(driver.window_handles[0])
                                switch_tab = False
                                keep_going = True
    if today == start_date:
        break



