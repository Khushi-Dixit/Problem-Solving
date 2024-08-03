#Find a peak element which is not smaller than its neighbours
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
