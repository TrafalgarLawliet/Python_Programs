import requests

link = 'https://corona.lmao.ninja/v2/countries/Germany?yesterday=true&strict=true&query'
info = requests.get(link).json()

continent = info['continent']
country = info['country']
today_cases = info['todayCases']
today_deaths = info['todayDeaths']
today_recovered = info['todayRecovered']
active_cases = info['active']
total_cases = info['updated']

print("Covid-19 Information")
print('Continent: ', continent)
print("Country: ", country)
print('Total Cases: ', total_cases)
print('Today Cases: ',today_cases)
print('Today Deaths: ', today_deaths)
print('Today Recovered: ', today_recovered)
print('Active Cases: ', active_cases)
