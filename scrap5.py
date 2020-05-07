#__________web scrapping to collect data(name,price,discount,offer,ratings) from flipkart____

import requests
from bs4 import BeautifulSoup as bs
response= requests.get('https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
obj=bs(response.content)
name=obj.findAll("div",{"class":"_3wU53n"})
print(len(name))
print(name[0].text)
price=obj.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
len(price)
print(price[0].text)

discount=obj.findAll("div",{"class":"_3auQ3N _2GcJzG"})
print(len(discount))
print(discount[0].text)
offer=obj.findAll("div",{"class":"VGWI6T"})
print(len(offer))
print(offer[0].text)
ratings=obj.findAll("span",{"class":"_38sUEc"})
print(len(ratings))
print(ratings[0].text)

a=[]
for i in range(15):
    a.append([name[i].text,':',price[i].text.replace(',',''),discount[i].text,offer[i].text,ratings[i].text.split('\xa0&\xa0')[0].replace(' Ratings','')])
    print(a[i])


#___________ For writing in json file____________
d={}
for i in a:
    d[i[0]]={'Price':i[1],'Discount':i[2],'Offer':i[3],'Rating':i[4]}
import json
with open('Phones.json','w') as x:
    json.dump(d,x)

#_________ For writing in csv file_____________
fields=['Name','Price','Discounted from','Offer','Ratings']
import csv
with open('mobiledata.csv','w',newline='',encoding="utf-8") as md:
    y=csv.DictWriter(md,fieldnames=fields)
    y.writeheader()
    for i in a:
        y.writerow({'Name':i[0],'Price':i[1],'Discounted from':i[2],'Offer':i[3],'Ratings':i[4]})