my_dict={'Andrey': 2005, 'Ivan': 2007, 'Daniel': 2010}
print(my_dict)
print(my_dict['Ivan'])
my_dict['Aleksey']=2000
print(my_dict['Aleksey'])
my_dict.update({'Oksana': 1999,
                'Denis': 2004})
my_dict.pop('Andrey')
print(my_dict)
my_set={1, 1, 2.5, 2.5, 'apple', 'apple'}
print(my_set)
my_set.add('Арбуз')
my_set.add(9)
my_set.discard(1)
print(my_set)