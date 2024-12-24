from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    uncommon = []

    for item in set(list1 + list2):
        diff = abs(count1[item] - count2[item])
        uncommon.extend([item] * diff)
    return uncommon

list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))