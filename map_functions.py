my_list = [1, 2, 3, 4, 5]

mapped = map(lambda x: x * 2, my_list)

mapped_list = list(mapped)

print(mapped_list) 

for i in mapped:
    print(i)