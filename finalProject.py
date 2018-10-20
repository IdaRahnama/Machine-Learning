from selenium import webdriver
import csv
from sklearn import tree
import re
import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='cars'
)

mycursor = mydb.cursor()
in1=input("Please enter the number of bedrooms:")
in2=input("Please enter the number of bathrooms:")
in3=input("please enter the square feet:")

for i in range(100):
	driver=webdriver.PhantomJS(executable_path="/Users/hamid/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
	url='https://www.realtor.com/realestateandhomes-search/Los-Angeles_CA/pg-%s'
	driver.get(url%i)


	ress = driver.find_elements_by_class_name("data-price")
	ress2 = driver.find_elements_by_xpath('//li[@data-label="property-meta-beds"]/span')
	ress3 = driver.find_elements_by_xpath('//li[@data-label="property-meta-baths"]/span')
	ress4 = driver.find_elements_by_xpath('//li[@data-label="property-meta-sqft"]/span')

	insert_data = ("INSERT INTO houseinfo4 ""(bd, ba, sqft, p) ""VALUES (%s, %s, %s, %s)")

	for j in range(30):
		num1 = re.sub("\D", "", ress2[j].text)
		num2 = re.sub("\D", "", ress3[j].text)
		num3 = re.sub("\D", "", ress4[j].text)
		num4 = re.sub("\D", "", ress[j].text)
		mycursor.execute(insert_data,(num1, num2, num3, num4))

		with open('test.csv', 'w', newline='') as fp:
			a = csv.writer(fp, delimiter=',')
			data=[[num1,num2,num3,num4]]
			a.writerows(data)
		mydb.commit()

x=[]
y=[]
with open('test.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[0:3])
        y.append(line[3])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
new_data = [[in1,in2,in3]]
answer = clf.predict(new_data)
print("The prediction of this house is:")
print(answer[0])


