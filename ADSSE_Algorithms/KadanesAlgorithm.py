import os
import psutil
import numpy as np
import tracemalloc


tracemalloc.start()
def kadanesAlgorithm(arr,size):

    globalMax = float('-inf')
    currentMax = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):
        currentMax = currentMax + arr[i]

        if (globalMax < currentMax):
            globalMax = currentMax
            start = s
            end = i

        if (currentMax < 0):
            currentMax = 0
            s = i+1

    return globalMax, start, end


arr = np.random.randint(-10,10,1000)

sum, start, end =  kadanesAlgorithm(arr,len(arr))

print("The maximum contiguous sum is", sum, "which is in the subarray from index", start, "to index", end)

current, peak = tracemalloc.get_traced_memory()

print(current, peak)
