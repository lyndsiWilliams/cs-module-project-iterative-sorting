def linear_search(arr, target):
    # Your code here

    # Loop through the length of the array
    for i in range(len(arr)):
        # If this iteration matches the target value
        if arr[i] == target:
            # Return the value
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    # Set the lowest value to 0
    low = 0
    # Set the highest value (boundary) to the length of the array - 1
    # -1 because when only 1 item is left, it doesn't need to be sorted
    high = len(arr) - 1

    # While the low value is <= the high value (boundary)
    while low <= high:
        # Find the midpoint
        mid = (high + low) // 2

        # Begin comparing the target to the midpoint
        if target == arr[mid]:
            return mid

        # If the target is < the midpoint
        if target < arr[mid]:
            # Cut out the right half of the array (greater than) and
            # Reassign the high value to the midpoint - 1
            high = mid - 1

        # If the target is > the midpoint
        if target > arr[mid]:
            # Cut out the left half of the array (less than) and
            # Reassign the low value to the midpoint + 1
            low = mid + 1


    return -1  # not found
