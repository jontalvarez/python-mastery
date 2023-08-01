import readrides

##Question 1: How many bus routes exist in Chicago?
rows = readrides.read_rides_as_dicts('../Data/ctabus.csv')
print(len({s['route'] for s in rows}))

##Question 2: How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?
from collections import Counter
totals = Counter()
for s in rows:
    totals[s['date']] += s['rides']
print(totals['02/02/2011'])

##Question 3: What is the total number of rides taken on each bus route?
from pprint import pprint 
totals = Counter()
for s in rows:
    totals[s['route']] += s['rides']

pprint(totals)
# print(sum([totals[s] for s in totals])) #total number of all bus rides

##Question 4: What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

