def max_num(num):
    max = num[0]
    for nums in num:
        if nums > max:
            max = nums
    return max

"""
Returns the maximum number of elements in a list.
:param num: The number of elements in the list.
:return: The maximum number of elements in the list.
"""