def quicksort(arr):
    if len(arr)<2:
        return arr
    
    mid = len(arr)//2
    pivot= arr[mid]
    middle = [i for i in arr if i==pivot]
    left_side = [i for i in arr if i<pivot]
    right_side = [i for i in arr if i>pivot]
    return quicksort(left_side)+middle+quicksort(right_side)

print(quicksort([3,2,2,2,2,2,2,2,2,1]))

print(quicksort([6235,235,347,1252,75,412,25,4,457,5412,4543,6,456,4235,6,43436,54,712,4,437]))
print(quicksort([6235,235,347,1252,75,412,25,4,457,5412,4543,6,456,4235,6,43436,54,712,4]))