import os
import psutil
import numpy as np
import tracemalloc


tracemalloc.start()
def maxCrossingSubArray(arr, l, m, h):

    left_sum = float('-inf')
    sum = 0

    for i in range(m, l-1, -1):
        sum = sum + arr[i]

        if (sum > left_sum):
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0

    for j in range(m + 1, h + 1):
        sum = sum + arr[j]

        if (sum > right_sum):
            right_sum = sum
            max_right = j

    return left_sum + right_sum, max_left, max_right


def maxSubArray(arr, l, h):

    if (l == h):
        return l, h, arr[l]

    else:
    # Find middle point
        m = (l + h) // 2


    left_sum, left_low, left_high = maxSubArray(arr, l, m)
    right_sum, right_low, right_high = maxSubArray(arr, m+1, h)
    cross_sum, cross_low, cross_high = maxCrossingSubArray(arr, l, m, h)

    if left_sum >= right_sum & left_sum >= cross_sum:
        return left_sum, left_low, left_high

    elif right_sum >= left_sum & right_sum >= cross_sum:
        return right_sum, right_low, right_high

    else:
        return cross_sum, cross_low, cross_high


arr = np.random.randint(-10,10,100)
n = len(arr)


sum, start, end = (maxSubArray(arr, 0, n-1))

print("The maximum contiguous sum is ", sum, ", which is in the subarray from index", start, "to index", end)

current, peak = tracemalloc.get_traced_memory()
print(current, peak)
