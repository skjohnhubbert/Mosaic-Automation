import urllib3

url = 'http://heartlandmosaic.com/sf01346307Mosaic/Reports/Sales' # write the url here

usock = urllib3.urlopen(url)
data = usock.read()
usock.close()

print (data)
