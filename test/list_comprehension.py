simple_list = [1, 2, 3, 4, 5, 6]
dup_list = [str(el) for el in simple_list if el > 3]

print(simple_list)

print(dup_list)

range_list = list(range(2, 10))

cal_list = [el for el in simple_list if el in range_list]

print(range_list)
print(cal_list)

my_dict = {
    'name': 'Jonathan',
    'age': 44
}

my_tuple_list = [('name','Jonathan'),('age',44),('last name','Caldwell'),('cash',41)]

my_mod_list = {key: value for key, value in my_tuple_list if value is not 42}

print(my_tuple_list)
print(my_mod_list)
print(f"My name is {my_mod_list['name']} {my_mod_list['last name']} and my age is {my_mod_list['age']}")

try:
    print(f"I have ${my_mod_list['cash']}")
except:
    print('I have no money')
    
print('-'*20)


my_mod_list = {key: value for key, value in my_tuple_list if value is not 41}

try:
    print(f"I have ${my_mod_list['cash']}")
except:
    print('I have no money now')
