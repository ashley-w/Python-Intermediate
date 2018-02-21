## 2. Array Comparisons ##

import numpy as np

countries_canada = world_alcohol[:,2] == 'Canada'


years_1984 = world_alcohol[:,0] == '1984'


## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:,2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986]

## 5. Replacing Values ##

year_1986 = world_alcohol[:,0] == '1986'
world_alcohol[:,0][year_1986] = '2014'

drink_wine = world_alcohol[:,3] == 'Wine'
world_alcohol[:,3][drink_wine] = 'Grog'

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[:,4][is_value_empty] = '0'


## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = '0'
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

print(canada_1986)

## 10. Calculating Consumption for Each Country ##

totals = {}
is_year = world_alcohol[:,0] == '1989'
year = world_alcohol[is_year,:]

for each in countries:
    is_country = year[:,2] == each
    country_consumption = year[is_country,:]
    alcohol_column = country_consumption[:,4]
    is_empty = alcohol_column == ''
    alcohol_column[is_empty] = '0'
    alcohol_column = alcohol_column.astype(float)
    alcohol_sums = alcohol_column.sum()
    # empty_strings = country_consumption[:,4] == ''
    # replaced_cons = country_consumption[:,4][empty_strings] = '0'
    # replaced_cons = replaced_cons.astype(float)
    # sum_of_cons = replaced_cons.sum()
    totals[each] = alcohol_sums
    
print(totals)

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None

for country in totals:
    consumption = totals[country]
    if consumption > highest_value:
        highest_value = consumption
        highest_key = country