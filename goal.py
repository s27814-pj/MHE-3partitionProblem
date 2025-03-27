from collections import Counter

def goal(list_of_units):
    list_of_sums=[0] *int(len(list_of_units) / 3)
    for i in range(len(list_of_units)):
        list_of_sums[list_of_units[i].get_index()] += list_of_units[i].get_value()
    return int(Counter(list_of_sums).most_common(1)[0][1])
