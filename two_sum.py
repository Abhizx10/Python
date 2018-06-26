"""
Leetcode #1 Two Sum - https://leetcode.com/problems/two-sum/description/

"""
def twosum_indices_linear(nums, target):
    numtoindexmap = {}
    for num1_index, num1 in enumerate(nums):
        num2 = target - num1
        print("Iterating through loop")
        try:
            num2_index = numtoindexmap[num2]
            print("New num2 index",num2_index)
        except KeyError:
            numtoindexmap[num1] = num1_index
            print("New num 1 indextoMap",numtoindexmap[num1])
        else:
            return num1_index, num2_index
