# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def updateDamages(damages = damages):
  newList = []
  conversion = {"M": 1000000, "B": 1000000000}
  for string in damages:
    if string == 'Damages not recorded':
      newList.append(string)
    else:
      mult = conversion[string[-1]] #checks the last character and replaces it according to the conv dictionary
      newList.append(float(string[:-1]) * mult)
      

  return newList

damages = updateDamages()

# write your construct hurricane dictionary function here:

def construct_hurricane_dict(
  names=names, 
  months=months, 
  years=years, 
  max_sustained_winds=max_sustained_winds, 
  areas_affected=areas_affected, 
  damages=damages, 
  deaths=deaths
  ):

  hurr_dict_by_name = {}
  for i in range(len(names)):
    hurr_dict_by_name.update({names[i]:
    {
      "Name" : names[i], 
      "Month" : months[i], 
      "Year" : years[i], 
      "Max sustained Wind" : max_sustained_winds[i], 
      "Areas affected" : areas_affected[i], 
      "Damages" : damages[i], 
      "Deaths" : deaths[i], 
    }

    })

  return hurr_dict_by_name

hurr_dict_by_name = construct_hurricane_dict()

print(hurr_dict_by_name["Cuba I"])


# write your construct hurricane by year dictionary function here:

def construct_hurricane_dict_by_year(
  names=names, 
  months=months, 
  years=years, 
  max_sustained_winds=max_sustained_winds, 
  areas_affected=areas_affected, 
  damages=damages, 
  deaths=deaths
  ):

  hurr_dict_by_year = {}
  for i in range(len(names)):
    current_year = years[i]
    hurr_dict = {
      "Name" : names[i], 
      "Month" : months[i], 
      "Year" : years[i], 
      "Max sustained Wind" : max_sustained_winds[i], 
      "Areas affected" : areas_affected[i], 
      "Damages" : damages[i], 
      "Deaths" : deaths[i], 
    }
    if current_year == years[i-1]:
      current_hurricane.append(hurr_dict)
    else:
      current_hurricane = [hurr_dict]
      hurr_dict_by_year.update({current_year:current_hurricane})

  return hurr_dict_by_year

hurr_dict_by_year = construct_hurricane_dict_by_year()

print(hurr_dict_by_year[2005])


# write your count affected areas function here:

def frequency_affected_areas(hurr_dict=hurr_dict_by_name):
  freq_dict = {}
  for hurricane in hurr_dict.values():
    for area in hurricane.get("Areas affected"):
      if freq_dict.get(area) is None:
        freq_dict[area] = 1
      else:
        freq_dict[area] += 1

  return freq_dict

freq_hurricane_areas = frequency_affected_areas()

print(freq_hurricane_areas)

# sort the affected areas dictionary by value:

sorted_freq_hurricane_areas = {key:value for key, value in sorted(freq_hurricane_areas.items(), key=lambda item: item[1], reverse=True)}

print(sorted_freq_hurricane_areas)


# write your find most affected area function here:

def most_affected_area():
  value = 0
  for item in freq_hurricane_areas.items():
    if item[1] > value:
      value = item[1]
      key = item[0]
  
  return "The area most affected by hurricanes is {key}, which was hit {value} times so far".format(key=key, value=value)

print(most_affected_area())



# write your greatest number of deaths function here:

def greatest_num_of_deaths(hurr_dict=hurr_dict_by_name):
  max_mortality = 0
  for hurricane in hurr_dict.values():
    number_of_deaths = hurricane.get("Deaths")
    if number_of_deaths > max_mortality:
      max_mortality = number_of_deaths
      max_mortality_hurr = hurricane.get("Name")

  return "The hurricane that caused the greatest number of deaths is {hurr}, taking {num_deaths} lives".format(hurr=max_mortality_hurr, num_deaths=max_mortality)

print(greatest_num_of_deaths())


# write your categorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def hurricane_mortality_rating(hurr_dict=hurr_dict_by_name):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

  for hurricane in hurr_dict.values():
    number_of_deaths = hurricane.get("Deaths")
    for rating in range(5):
      if number_of_deaths == 0:
        hurricane_rating = 0
      elif number_of_deaths > mortality_scale[rating]:
        hurricane_rating = rating + 1

    hurricanes_by_mortality.get(hurricane_rating).append(hurricane)

  return hurricanes_by_mortality

print(hurricane_mortality_rating())
    


# write your greatest damage function here:

def greatest_damage(hurr_dict=hurr_dict_by_name):
  greatest_damage_cost = 0
  for hurricane in hurr_dict.values():
    damages_cost = hurricane.get("Damages")
    if (isinstance(damages_cost, str) == False) and damages_cost > greatest_damage_cost:
      greatest_damage_cost = damages_cost
      greatest_damage_hurr = hurricane.get("Name")

  return "The hurricane that caused the greatest damage was {hurr_name}, dealing USD {greatest_damage_cost} in damages".format(
    hurr_name=greatest_damage_hurr,
    greatest_damage_cost="{:,}".format(greatest_damage_cost) # added comma separator to make it easier to read
    ) 

print(greatest_damage())



# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def hurricane_damage_rating(hurr_dict=hurr_dict_by_name):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}

  for hurricane in hurr_dict.values():
    damages_cost = hurricane.get("Damages")
    if isinstance(damages_cost,float):
      for rating in range(5):
        if damages_cost == 0:
          hurricane_rating = 0
        elif damages_cost > damage_scale[rating]:
          hurricane_rating = rating + 1
    
      hurricanes_by_damage.get(hurricane_rating).append(hurricane)
      
  return hurricanes_by_damage

print(hurricane_damage_rating())