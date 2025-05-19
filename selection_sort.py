def smallest_element(arr):
    smallest = arr[0]
    smallest_index =0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index = i
    
    return smallest_index

def selection_sort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(arr)):
        smallest_index = smallest_element(copiedArr)
        newArr.append(copiedArr.pop(smallest_index))
    return newArr

array = [1,46,235,12,124,745,24,35]
print(selection_sort(array))
print(array)

        
        