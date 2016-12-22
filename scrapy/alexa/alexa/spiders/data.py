#############################################################################################
# @Author : Omkar Nath                                                                      #
# @Email  : omkar@startupflux.com                                                           #
# @About  : A script which scrapes site data from oddup.com                                 #
#                                                                                           #
#         : Before running check the requirement.txt file                                   #
#         : 1) Connect to a MongoDB document collection                                     #
#         : 2) Display all of the documents in a collection                                 #
#         : 3) Insert a document                                                            #
#############################################################################################

# input data from mongodb
# scrape using BeautifulSoup
# store in the json format or mongodb
 
import time
import json
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

# replace the "" in the line below with your MongoLab connection string
# you can also use a local MongoDB instance
connection = MongoClient("mongodbconnectionstring")
 
# connect to the website url database and the ctec121 collection
# input your own connection here
db = connection.students.ctec121
 

alexa_scraping_record = {}
flag = True
# find all documents
results = db.find()

# create a empty json file name as empty.json
# empty.json is in the root directory of the ths script
with open('empty.json') as f:
    data = json.load(f)

# display documents from collection
# in FIELD schema input name of company and company url
for record in field_names:
	print(record['website'] + ',',record['name'])
	company_name = record['website']
	alexa_link = "http://data.alexa.com/data?cli=10&dat=snbamz&url=" + company_name
	r = requests.get(alexa_link)
	r.content
	soup = BeautifulSoup(r.content)
	# print soup.prettify()

	timestamp = time.time()

	reach_rank = ""
	for link in soup.find_all("reach"):
		reach_rank = link.get("rank")
	    print link.get("rank")

	if not reach_rank:
		reach_rank = None

	rank_delta = ""
	for link in soup.find_all("rank"):
		rank_delta = link.get("delta")
		print link.get("delta")

	if not rank_delta:
		rank_delta = None

	country_code = ""
	for link in soup.find_all("country"):
		country_code = link.get("code")
		print link.get("code")

	if not country_code:
		country_code = None

	country_name = ""
	for link in soup.find_all("country"):
		country_name = link.get("name")
		print link.get("name")

	if not country_name:
		country_name = None

	country_rank = ""
	for link in soup.find_all("country"):
		country_rank = link.get("rank")
		print link.get("rank")

	if not country_rank:
		country_rank = None

	alexa_dict = {
					'reach_rank'  : reach_rank
					'rank_delta'  : rank_delta
					'country_code': country_code
					'country_name': country_name
					'country_rank': country_rank
					'timestamp'   : timestamp
				}

	

	data.update(alexa_dict)

	with open('empty.json', 'w') as f:
	    json.dump(data, f)


# adding all alexa data of various urls
with open('empty.json') as f:
    alexa_scraping_record = json.load(f)

# insetring to clean DB
# change path for clean DB
db.insert(alexa_scraping_record)
connection.close()



'''
while (flag):
   student_name,student_grade = input("Enter student name and grade: ").split(',')
   student_record = {'name':student_name,'grade':student_grade}
   db.insert(student_record)
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
      flag = False

'''