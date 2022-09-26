"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

"""
my_dict = {}
List = [1, 2, 3, 4]
contains_duplicate = False
for i in List:
    if i not in my_dict.keys():
        my_dict[i] = 1
    else:
        my_dict[i] = my_dict[i] + 1
        contains_duplicate = True
print(contains_duplicate)




