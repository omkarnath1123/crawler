import urllib2
import re

url = "https://www.amazon.in/"
url1 = "https://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=mobile"

store_limit = 2000
#connect to a URL
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://www.amazon.in.*?dp.*?)"', html)
type(links)
import csv
outputFile = open('output.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(links)

print links