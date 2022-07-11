d = {'key1':'value1', 'key2':'value2'}
print(d)
print(d['key1'])

salaries = {'John': 20,'Sally':30,'Sammy':15}
salaries['Cindy'] = 100
print(salaries['Sally'])
print(salaries['Cindy'])
print("the salary for Cindy, the CEO, is: ")
print(salaries['John'])
salaries["John"] = salaries['John'] + 23
print(salaries['John'])
print("-----------------")
people = {'John': [1,2,3],'Sally':[40,10,30]}
print(people['John'])
print(people['Sally'][0])
print("-----------------")
people = {'John': {'salary':10, 'age':30}}
print(people["John"]['age'])
print("-----------------")

salaries = {'John': 20,'Sally':30,'Sammy':15}
print(salaries.keys())
print(salaries.values())
print(salaries.items())
