import json

from numpy import double

maleKey = 0
femaleKey = 0

f = open('role.json')
senators = json.load(f)
for key in senators['objects']:
    if key["person"]["gender"] == "male":
        maleKey+=1
    else:
        femaleKey+=1
genderdict = ['male', 'female']
numberdict = [maleKey, femaleKey]


import matplotlib.pyplot as plt

plt.bar(genderdict, numberdict)
plt.title('Gender Breakdown in the Senate')
plt.xlabel('gender')
plt.ylabel('number of males/females in the Senate')
plt.show()



import csv
import pandas as pd
df = pd.read_csv("crime.csv", header = 1)
exampleFile = open('crime.csv')
exampleReader = csv.reader(exampleFile)

homicideA = []
homicideB = []

for row in exampleReader:
    if row[0] == '2':
        homicideA.append(double(row[4]))
       
    if row[0] == '30':
        homicideB.append(double(row[4]))

yeardict = ['2005', '2010', '2015', '2020']



import matplotlib.pyplot as plt

plt.plot(yeardict,homicideA, label = 'Africa')
plt.plot(yeardict,homicideB, label = 'Eastern Asia')
plt.title('Comparison of Homicides in Africa and Eastern Asia')
plt.xlabel('Year')
plt.ylabel('Intentional homicide rates per 100,000')
plt.legend()
plt.show()
