# Enter your code here. Read input from STDIN. Print output to STDOUT
my_list = []

n = int(input("Number of elements : "))

for x in range(0, n):
    element = int(input())
 
    my_list.append(element)
print(my_list)

import statistics

mean = statistics.mean(my_list)
print (round((mean),1))

median = statistics.median(my_list)
print (round((median),1))

from collections import Counter

c = Counter(my_list)
max_number_count = c.most_common(1)[0][1]
modes = (item for item, count in c.items() if count == max_number_count) 
min_mode = min(modes)
print(min_mode)
