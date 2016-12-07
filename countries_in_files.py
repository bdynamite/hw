# Создание нового словаря
# new_dict = dict() # {}

#country_1 = {'name': 'Thailand, 'sea': True}
#country_2 = {'name': 'Hungary', 'sea': False}

# Подход 1 - списки
#countries = [
	#{'name': 'Thailand', 'sea': True, 'schengen': False, 'average_temperature': 30, 'currency_rate': 1.8},
	#{'name': 'Hungary', 'sea': False, 'schengen': True, 'average_temperature': 10, 'currency_rate': 0.3},
	#{'name': 'Germany', 'sea': True, 'schengen': True, 'average_temperature': 5, 'currency_rate': 80},
	#{'name': 'Japan', 'sea': True, 'schengen': False, 'average_temperature': 15, 'currency_rate': 0.61}
	#]

def save_json(data):
	import json
	with open('all_coutries.json', 'w') as file:
		json.dump(data, file)

def save_xml(data):
	import xml.etree.ElementTree as ET
	root = ET.Element('countries')
	for country, parametres in data.items():
		new_group = ET.SubElement(root, country)
		for parameter, value in parametres.items():
			new_group.set(parameter, str(value))
	tree = ET.ElementTree(root)
	tree.write('all_countries.xml')

def save_yaml(data):
	import yaml
	with open('all_countries.yaml', 'w') as file:
		yaml.dump(data, file, default_flow_style = True)

def save_csv(data):
	import csv
	with open('all_countries.csv', 'w') as file:
		writer = csv.writer(file)
		writer.writerow(['country', 'parameter', 'value'])
		for country, parametres in data.items():
			for parameter, value in parametres.items():
				writer.writerow([country, parameter, str(value)])




budget = 40000	
	
# Подход 2 - словарь
countries = {
	#'Cuba': data_about_Cuba,
	'Thailand': {'sea': True, 
				'schengen': False, 
				'average_temperature': 30, 
				'currency_rate': 1.8,
				'cost_of_a_day': 600},
	'Hungary': {'sea': False, 
				'schengen': True, 
				'average_temperature': 10, 
				'currency_rate': 0.3,
				'cost_of_a_day': 3400},
	'Germany': {'sea': True, 
				'schengen': True, 
				'average_temperature': 5, 
				'currency_rate': 80,
				'cost_of_a_day': 25},
	'Japan': {'sea': True, 
				'schengen': False, 
				'average_temperature': 15, 
				'currency_rate': 0.61,
				'cost_of_a_day': 1700},
	'Brazil': {'sea': True,
				'schengen': False,
				'average_temperature': 25,
				'currency_rate': 20,
				'cost_of_a_day': 50},
	'Norway': {'sea': True,
				'schengen': True,
				'average_temperature': -5,
				'currency_rate': 80,
				'cost_of_a_day': 40},
	'Chad': {'sea': False,
				'schengen': False,
				'average_temperature': 30,
				'currency_rate': 0.03,
				'cost_of_a_day': 35000},
	'New-Zeland': {'sea': True,
				'schengen': False,
				'average_temperature': 20,
				'currency_rate': 60,
				'cost_of_a_day': 17},
	'Andorra': {'sea': False,
				'schengen': True,
				'average_temperature': 20,
				'currency_rate': 80,
				'cost_of_a_day': 38}
	}
	
# Как заполнить словарь
# d = dict()
# d['name'] = 'Thailand'
	
# Множества - удобная структура для операций пересечения и объединения, поддерживает уникальность элементов	
# В отличие от списков, элементы множества не упорядочены
schengen_countries = set()
sea_countries = set()
warm_countries = set()
expensive_countries = set()
	
for country_name, properties in countries.items():
	if properties['cost_of_a_day'] * properties['currency_rate'] * 30 > budget:
		expensive_countries.add(country_name)
	if properties['average_temperature'] >= 20:
		warm_countries.add(country_name)	
	if properties['schengen']:
		schengen_countries.add(country_name)
	if properties['sea']:
		sea_countries.add(country_name)
		
		
print ('Sea countries: {}'.format(sea_countries))
print ('Schengen countries: {}'.format(schengen_countries))

#print ('Страны в шенгене и с морем: ', schengen_countries & sea_countries)


# Форматирование вывода
#money_amount = 10000
#for country in countries:
#	currency_amount = money_amount / country['currency_rate']
#	print('У нас будет %.3f денег в местной валюте' % currency_amount)


sea_schengen_countries = schengen_countries & sea_countries

# Подход со списками словарей
#for country_name in sea_schengen_countries:
#	for country in countries:
#		if country['name'] == country_name:
#			print(country)
#			break

# Подход со словарем словарей
for country_name in sea_schengen_countries:
	print(country_name, countries[country_name])

## HW	
sea_or_schengen_countries = schengen_countries | sea_countries

print('Можно поехать в следующие страны: {}'.format(((warm_countries & sea_countries) | schengen_countries) - expensive_countries))

save_json(countries)

save_xml(countries)

save_yaml(countries)

save_csv(countries)



