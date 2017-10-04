import urllib2

response = urllib2.urlopen('https://heartlandmosaic.com/sf01346307Mosaic')
page_source = response.read()
