import random
import time
fruits = ["apple","banana","grape","avocado"]

fruit_choice = random.choice(fruits)
random_num = random.randint(1,10)
print("random number: ", random_num)

time.sleep(3)
print("random fruit", fruit_choice)