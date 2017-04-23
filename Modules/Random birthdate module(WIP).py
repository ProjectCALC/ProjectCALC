from datetime import datetime
import random
 
year = random.choice(range(1950, 2001))
month = random.choice(range(1, 13))
day = random.choice(range(1, 29))
birth_date = datetime(year, month, day)
