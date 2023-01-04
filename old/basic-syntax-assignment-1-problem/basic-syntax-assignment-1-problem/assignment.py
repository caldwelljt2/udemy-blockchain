#1 Create two variables – one with your name and one with your age
my_name = input("Name: ")
my_age = input("Age: ")

#2 Create a function which prints your data as one string
def print_data(name, age):
    print(name + " " + age)

#3 Create a function which prints ANY data (two arguments) as one string
def print_any_data(val1, val2):
    print(str(val1) + str(val2))
    
#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def decades(yrs):
    print(f"You have been alive { int(yrs) // 10 } decades")

print_data(my_name, my_age)
print_any_data(my_name, my_age)
print_any_data("string", 1)
print_any_data(True, 0.55)
print_any_data([1,2], (3,4))
print_any_data({'diction':'ary'}, False)
# print_any_data(my_name, my_age)
decades(my_age)