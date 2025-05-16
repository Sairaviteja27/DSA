def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high)//2
        guess=arr[mid]
        if item==guess:
            return mid
        elif item<guess:
            high=mid-1
        else:
            low=mid+1


my_arr = [1,5,7,9,11,73,89,121,156,193]
print(binary_search(my_arr,11))
print(binary_search(my_arr,156))