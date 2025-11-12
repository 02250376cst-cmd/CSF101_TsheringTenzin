#lab steps
#step 1:  Implement Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

def Binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left+right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return Binary_search_recursive(arr, target, mid+1, right)
    else:
        return Binary_search_recursive(arr, target, left, mid-1)

test = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test, 6)
print(f"linear search: Index of 6 is {result}")

test_list_sorted = sorted(test)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

result = Binary_search_recursive(test_list_sorted)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")
