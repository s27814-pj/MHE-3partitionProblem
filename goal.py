import statistics
from collections import Counter

def goal(list_of_units):
    list_of_sums=[0] *int(len(list_of_units) / 3)
    for i in range(len(list_of_units)):
        list_of_sums[list_of_units[i].get_index()] += list_of_units[i].get_value()
    return int(Counter(list_of_sums).most_common(1)[0][1])
#wuiecej bliskosc i=do sumy

def goal2(values,index):
    list_of_sums = [0] * int(len(values) / 3)
    for i in range(len(values)):
        list_of_sums[index[i]] += values[i]
    # print('goalin',statistics.variance(list_of_sums))
    return int(Counter(list_of_sums).most_common(1)[0][1])

def goal3(values,index):
    list_of_sums = [0] * int(len(values) / 3)
    for i in range(len(values)):
        list_of_sums[index[i]] += values[i]
    return statistics.variance(list_of_sums)*(-1)
