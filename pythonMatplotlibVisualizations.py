data_directory = 'C:/covid/covid_deaths.csv'


'''
Read New cases of each country and show it using a line plot
Total cases for each country.
Generate line plot must include the
X label name = Country
Y label name= Total cases

'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(data_directory)
caseList = df['total_cases'].tolist()
countryList =  df['location'].tolist()
plt.plot(caseList, countryList, label = 'Increase in covid cases')
plt.xlabel('Case number')
plt.ylabel('Country names')
plt.xticks([10,100,1000,10000,100000,1000000])
plt.title('Covid cases per country')
plt.yticks(countryList)
plt.show()

'''
Get total count of cases of each country
Show line plot with the following Line Style dotted and Line-color should be red
Show legend at the lower right location
X label name = Case Number
Y label name = Sold units number
Add a circle marker.
Line marker color as read
Line width should be 3
'''
df = pd.read_csv(data_directory)
caseList = df['total_cases'].tolist()
countryList =  df['location'].tolist()
plt.plot(caseList, countryList, label = 'Covid cases per country',
         color='r', marker='o',markerfacecolor='k',
         linestyle='--',linewidth=3)
plt.xlabel('Case number')
plt.ylabel('Country names')
plt.xticks([10,100,1000,10000,100000,1000000])
plt.title('Covid cases per country')
plt.yticks(countryList)
plt.show()
