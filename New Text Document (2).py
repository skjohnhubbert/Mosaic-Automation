def BuildFireFoxDriver():
    fp = webdriver.FirefoxProfile('/Python Projects/test')
    driver = webdriver.Firefox(firefox_profile=fp)
    driver.get('https://heartlandmosaic.com/sf01346307Mosaic')

