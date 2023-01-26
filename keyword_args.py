def my_func(*args, **kwargs):
    print(args)
    print(kwargs['name'])
    for key, argument in kwargs.items():
        print(key, argument)
    
my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name='John', age=36)
 