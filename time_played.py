from collections import Counter
from reader import streaming_history

YEAR = 2020

total = 0

for item in streaming_history():
    if item.timestamp.year != YEAR:
        continue

    total += item.ms_played


print(f"{total/1000:0.2f} seconds")
print(f"{total/1000/60:0.2f} minutes")
print(f"{total/1000/60/60:0.2f} hours")
print(f"{total/1000/60/60/24:0.2f} days")
print(f"{total/1000/60/60/24/30:0.2f} months")
print(f"{total/1000/60/60/24/365:0.2f} years")
