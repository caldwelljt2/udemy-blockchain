import random
import datetime

random_num_0_1 = random.random()
random_num_1_10 = random.randint(1, 10) 
random_num_1_10_v2 = int(random.random() * 10)
print('random number 0-1:', random_num_0_1)
print('random number 0-10:',random_num_1_10)
print('random number 0-10 alt:', random_num_1_10_v2)

random_num_big = random.randint(1, 10000)
now = datetime.datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
unique_value = str(timestamp) + str(random_num_big)
print('random unique number :', unique_value)
