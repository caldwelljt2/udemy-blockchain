def sample_function():
    return "This is a sample function"
    

# 1) Write a normal function that accepts another function as an argument.
# Output the result of that other function in your “normal” function.

def process_function(function):
    print(f'processing {function} and returning' )
    return function()

# process_function(sample_function)

# 2) Call your “normal” function by passing a lambda function – which performs 
# any operation of your choice – as an argument.

# process_function(lambda x, y: x + y, 2, 3)

# 3) Tweak your normal function by allowing an infinite amount of arguments on 
# which your lambda function will be executed.


def process_function(in_function, *args):
  output = []
  for arg in args:
    output.append(in_function(arg))
  print("{:^20}".format("Is Odd"))
  for i in output:
    print("{:^20}".format(f'{i}'))

process_function(lambda x: bool(x%2), 1, 22, 331, 42, 99)

# Output:
#     Output
#         1
#         4
#         9
#        16
#        25

# 4) Format the output of your “normal” function such that numbers look nice
# and are centered in a 20 character column.

