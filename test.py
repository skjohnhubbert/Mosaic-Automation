from selenium import webdriver
fp = webdriver.FirefoxProfile('C:/Users/sahubbert/AppData/Roaming/Mozilla/Firefox/Profiles/n5262fav.python')
browser = webdriver.Firefox(fp)
type(browser)
browser.get('https://heartlandmosaic.com/sf01346307Mosaic')
