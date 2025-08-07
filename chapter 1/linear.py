def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

arr1 = [10, 20, 30, 40, 50]
target = 50
result = linear_search(arr1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")