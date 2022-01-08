# Python Dictionaries Challenge Project: Hurricane Analysis
# Last updated on 13/12/2021

'''
Project Goals:
Write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. 
Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.
'''

from collections import defaultdict

#region [Data provided]
# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# names of the hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

#  months in which the hurricanes occurred
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years in which the hurricanes occurred
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (miles per hour) of the hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# list of different areas affected by each of the hurricanes
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# total number of deaths caused by each of the hurricanes
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
#endregion

'''
Write a function that returns a new list of updated damages where the recorded data is converted to float values (B stands for billions and M stands for millions) and the missing data is retained as 'Damages not recorded'.
'''
def update_damages(damages):
    conversion = {'M': 1000000, 'B': 1000000000}
    updated_damages = []

    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        elif damage.endswith('M'):
            updated_damages.append(float(damage.strip('M')) * conversion['M'])
        elif damage.endswith('B'):
            updated_damages.append(float(damage.strip('B')) * conversion['B'])
    return updated_damages

updated_damages = update_damages(damages)

'''
Additional data collected on the 34 strongest Atlantic hurricanes are provided in a series of lists. The data is organized such that the data at each index, from 0 to 33, corresponds to the same hurricane. 
Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year, Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
'''
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricane_dict = {}

    for name in names:
        i = names.index(name)
        hurricane_dict[i] = {'Name': names[i], 
                            'Month': months[i], 
                            'Year': years[i], 
                            'Max Sustained Wind': max_sustained_winds[i], 
                            'Areas Affected': areas_affected[i], 
                            'Damage': updated_damages[i], 
                            'Deaths': deaths[i]}
    return hurricane_dict

hurricane_dict = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

'''
Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
'''
def hurricane_by_year(hurricane_dict):
    hurricane_by_year_dict = {}

    for year in years:
        hurricane_by_year_dict[year] = [hurricane for hurricane in hurricane_dict.values() if hurricane["Year"] == year]
    return hurricane_by_year_dict

hurricane_by_year(hurricane_dict)

'''
Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
'''
def count_affected_area(hurricane_dict):
    count_affected_area_dict = {}            
    # a defaultdict is created with default value as 0.
    default_dict = defaultdict(int)

    for hurricane in hurricane_dict:
        # get value of nested dictionary - example_dict.get('key1', {}).get('key2')
        areas_values = hurricane_dict.get(hurricane, {}).get('Areas Affected')        
        for affected_area in areas_values:
            default_dict[affected_area] += 1
    count_affected_area_dict = dict(default_dict.items())
    return count_affected_area_dict

count_affected_area_dict = count_affected_area(hurricane_dict)

'''
Write a function that finds the area affected by the most hurricanes, and how often it was hit.
'''
def most_affected_area(count_affected_area_dict):
    area_affected = ''
    highest_hit_count = 0

    for i in count_affected_area_dict.keys():
        if count_affected_area_dict[i] > highest_hit_count:
            area_affected = i
            highest_hit_count = count_affected_area_dict[i]
    print(f'{area_affected} is the most affected area, with a hit count of {highest_hit_count}.')

most_affected_area(count_affected_area_dict)

'''
Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
'''
def greatest_number_of_deaths(hurricane_dict):
    hurricane = ''
    greatest_number_of_deaths = 0

    for i in hurricane_dict:
        if hurricane_dict[i].get('Deaths') > greatest_number_of_deaths:
            hurricane = hurricane_dict[i].get('Name')
            greatest_number_of_deaths = hurricane_dict[i].get('Deaths')
    print(f'The most deadly hurricane is {hurricane}, it caused a total of {greatest_number_of_deaths} deaths.')

greatest_number_of_deaths(hurricane_dict)

'''
Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.
mortality_scale = { 0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.
'''
def catgeorize_by_mortality(hurricane_dict):
    mortality_scale = { 0: 0,
                        1: 100,
                        2: 500,
                        3: 1000,
                        4: 10000}
    hurricane_by_mortality =  { 0: [],
                                1: [],
                                2: [],
                                3: [],
                                4: [],
                                5: []}

    for hurricane in hurricane_dict.keys():
        name = hurricane_dict[hurricane].get('Name')
        deaths = hurricane_dict[hurricane]["Deaths"]
        if deaths == mortality_scale[0]:
            hurricane_by_mortality[0].append(name)
        elif deaths <= mortality_scale[1]:
            hurricane_by_mortality[1].append(name)
        elif deaths <= mortality_scale[2]:
            hurricane_by_mortality[2].append(name)
        elif deaths <= mortality_scale[3]:
            hurricane_by_mortality[3].append(name)
        elif deaths <= mortality_scale[4]:
            hurricane_by_mortality[4].append(name)
        else:
            hurricane_by_mortality[5].append(name)
    return hurricane_by_mortality

catgeorize_by_mortality(hurricane_dict)

'''
Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
'''
def greatest_damage(hurricane_dict):
    hurricane = ''
    greatest_damage = 0

    for i in hurricane_dict:
        if type(hurricane_dict[i].get('Damage')) == str:
            continue
        elif hurricane_dict[i].get('Damage') > greatest_damage:
            hurricane = hurricane_dict[i].get('Name')
            greatest_damage = round(hurricane_dict[i].get('Damage'))
    print(f'The hurricane {hurricane} costed the most damage - a loss of ${greatest_damage}.') 

greatest_damage(hurricane_dict)

'''
Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
'''
def catgeorize_by_damage(hurricane_dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    hurricane_by_damage =  {0: [],
                            1: [],
                            2: [],
                            3: [],
                            4: [], 
                            5: [],
                            'Not recorded': []}

    for hurricane in hurricane_dict.keys():
        name = hurricane_dict[hurricane].get('Name')
        damage = hurricane_dict[hurricane]['Damage']
        if type(damage) == str:
            hurricane_by_damage['Not recorded'].append(name)
            continue
        elif damage == damage_scale[0]:
            hurricane_by_damage[0].append(name)
        elif damage <= damage_scale[1]:
            hurricane_by_damage[1].append(name)
        elif damage <= damage_scale[2]:
            hurricane_by_damage[2].append(name)
        elif damage <= damage_scale[3]:
            hurricane_by_damage[3].append(name)
        elif damage <= damage_scale[4]:
            hurricane_by_damage[4].append(name)
        else:
            hurricane_by_damage[5].append(name)
    return hurricane_by_damage

catgeorize_by_damage(hurricane_dict)