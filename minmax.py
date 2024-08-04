def find_min_max(arr):
    if not arr:
        return []

    min_element = arr[0]
    max_element = arr[0]

    for num in arr[1:]:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

    return [min_element, max_element]

# Examples
print(find_min_max([3, 2, 1, 56, 10000, 167]))   # Output: [1, 10000]
print(find_min_max([1, 345, 234, 21, 56789]))   # Output: [1, 56789]
print(find_min_max([56789]))                    # Output: [56789, 56789]
