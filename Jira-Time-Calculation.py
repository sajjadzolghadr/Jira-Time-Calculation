import csv
from collections import defaultdict
# add your jira csv file 
data = open('your_file.csv' , encoding='utf-8')
csv_data = csv.reader(data)
data_list = list(csv_data)

nahaE=[]
for line in data_list[1:]:
    nahaE.append(line[13] + ' ' + line[37])

sums = defaultdict(int)

for item in nahaE:
    parts = item.split()
    if len(parts) == 2:
        name , value = parts[0] , int(parts[1])
        sums[name] += value

for name in sums:
    sums[name] //= 3600

print(dict(sums))

