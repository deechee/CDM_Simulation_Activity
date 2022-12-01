# country & city

import pandas as pd

country_city_raw = pd.read_csv('worldcities.csv')
country_city = country_city_raw[['city_ascii', 'country']]

countries = ['Japan', 'France']


def sample_country_city(country_city, countries, n=500):
    cc_list=[]
    for i in range(n):
        x = 0
        while x == 0:
            data = pd.DataFrame.sample(country_city).values[0]
            country = data[1]

            if country in countries:
                cc_list.append(data)
                x=1
    return cc_list
country_city_list = sample_country_city(country_city, countries) #



print(country_city_list)