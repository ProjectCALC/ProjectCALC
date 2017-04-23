from random import randrange
import datetime 


def random_date(start,l):
   current = start
   while l >= 0:
    current = current + datetime.timedelta(minutes=randrange(10))
    yield current
    l-=1



startDate = datetime.datetime(2013, 9, 20,13,00)


for x in reversed(list(random_date(startDate,10))):
    print x.strftime("%d/%m/%y %H:%M")
