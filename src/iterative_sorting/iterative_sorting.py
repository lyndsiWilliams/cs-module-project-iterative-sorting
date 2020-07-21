# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Set the current index (boundary) to i
        cur_index = i

        # Set the smallest value as the value at "current index" (i)
        smallest_value = arr[cur_index]
        # Set the smallest index as the current index (i)
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # Loop through the array, setting the beginning as the cur_index
        # and the end as the length of the array
        for unsorted_index in range(cur_index, len(arr)):
            # If this iteration is smaller than the smallest value...
            if arr[unsorted_index] < smallest_value:
                # Reassign the smallest value to the current iteration
                smallest_value = arr[unsorted_index]
                # The smallest index is now the unsorted index
                # This value will now be ran through this loop
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here

        # Criss-cross! (swap current index and smallest index)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # Loop through the length of the array
    # -1 because when only 1 item is left, it doesn't need to be sorted
    for i in range(len(arr) - 1):
        # In every iteration of the outer loop, one number gets sorted.
        # This inner loop only runs the unsorted part
        for j in range(len(arr) - i - 1):
            # If two adjacent elements are in the wrong order...
            if arr[j] > arr[j + 1]:
                # Criss-cross! (swap the elements)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here

    if not len(arr):
        return arr

    # Use list comprehension to create a bucket for each value
    bucket = [0 for i in range(max(arr) + 1)]

    # Fill the buckets with this loop
    for i in arr:
        # No negative numbers allowed!
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        # Each time a value appears in an iteration, fill the bucket and
        # Add 1 to the bucket count
        bucket[i] += 1

    # Start the index at 0 (first position)
    ndx = 0
    # Refill the array with the buckets' compressed data
    for i in range(len(bucket)):
        # For each bucket from smallest to largest...
        while 0 < bucket[i]:
            # add the index of the bucket to the input array
            arr[ndx] = i
            # Increment the index by 1 to continue the count
            ndx += 1
            # Decrease the bucket count
            bucket[i] -= 1
            # This will run until the bucket count is 0

    return arr
