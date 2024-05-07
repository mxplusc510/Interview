def findDuplicates(arr):
    duplicates = []
    for num in arr:
        index = abs(num) - 1
        if arr[index] < 0:
            duplicates.append(abs(num))
        else:
            arr[index] = -arr[index]
    return duplicates

print(findDuplicates([1, 2, 3, 4, 5])) 
print(findDuplicates([1, 2, 3, 3, 4, 5])) 
print(findDuplicates([1, 1, 2, 3, 3, 4, 5]))
print(findDuplicates([1, 1, 1, 2, 3, 3, 3, 4, 5, 5])) 
