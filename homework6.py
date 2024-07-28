my_dict = {'Anna': 1982, 'Natasha': 1968, 'Vitalii': 1985, 'Veronika': 2020}
print(my_dict)
print(my_dict['Natasha'])
my_dict['Roksana'] = 2018
print(my_dict)
my_dict.update({'Matvei': 2008,
                'Anton': 1983})
print(my_dict)
del my_dict['Natasha']
print(my_dict)
my_set = {1, 2, 3, 1, 2, 3, 'a', 'b', 'c', 'b', 'c'}
print(my_set)
my_set.add(5)
my_set.add('d')
my_set.remove(2)
print(my_set)