#Find a peak element which is not smaller than its neighbours
#binary search 
#input = 10, 20, 15, 2, 23, 90, 67
#output=20
#O(n) time complexity
def find_peak_element(arr):
    n = len(arr)
    
    # Handle edge cases
    if n == 1:
        return arr[0]
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]
    
    # Binary search to find a peak element
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if mid is a peak element
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]
        
        # If the middle element is part of the decreasing slope
        if mid > 0 and arr[mid - 1] > arr[mid]:
            right = mid - 1
        else:  # If the middle element is part of the increasing slope
            left = mid + 1
    
    return -1  # This case should never be reached

# Function to take input and print the result
def main():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    peak = find_peak_element(arr)
    print(f"Peak element: {peak}")

if __name__ == '__main__':
    main()


#binary search with output 90 and time complexcity=O(log n) and space = O(1)
def find_peak_element(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        # If mid is greater than next element, the peak is in the left half (including mid)
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            # If mid is less than next element, the peak is in the right half
            low = mid + 1

    return arr[low]

# Function to take input and print the result
def main():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    peak = find_peak_element(arr)
    print(f"Peak element: {peak}")

if __name__ == '__main__':
    main()






#linear search 
#input =10, 20, 15, 2, 23, 90, 67
#output=90
#time complexity is O(n).
#space complexity = O(1)

def find_peak_element(arr):
    # Initialize the peak element as the first element
    peak = arr[0]
    
    # Iterate through the array to find the maximum element
    for num in arr:
        if num > peak:
            peak = num
            
    return peak

# Function to take input and print the result
def main():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    peak = find_peak_element(arr)
    print(f"Peak element: {peak}")

if __name__ == '__main__':
    main()


#Conclusion
#The binary search approach is the best among the three in terms of efficiency due to its O(log n) time complexity. It is suitable for large arrays and provides a significant performance advantage over the linear search approaches.

#However, if simplicity and ease of understanding are more important, the linear search approach is preferable. It is straightforward and works well for small to medium-sized arrays.

#Therefore, the choice depends on the specific requirements:

#For efficiency with large datasets, use the binary search approach.
#For simplicity and ease of understanding, use the linear search approach.



# to find the no of pain which can generated the value of k after addition from and array with no duplicates
arry = [5, 7, 1, -1]
k = 6
sum_pairs = 0
l = []

for i in range(len(arry)):
    for j in range(i + 1, len(arry)):
        if arry[i] + arry[j] == k:
            pair = sorted([arry[i], arry[j]])  # Sort the pair to handle order (e.g., (1, 5) and (5, 1))
            if pair not in l:  # Check if the pair is already counted
                l.append(pair)  # Add the unique pair to the list
                sum_pairs += 1  # Increment the count

print(sum_pairs)

