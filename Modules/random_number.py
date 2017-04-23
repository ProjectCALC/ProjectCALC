import random
import time
import fighting

number = random.randint(1, 10)
while number != 7:
    number = random.randint(1, 10)
if number == 7:
    fighting.main()
