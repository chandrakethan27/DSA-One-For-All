# Initial array to be sorted
arr = [7, 2, 5, 1, 9, 4, 4]

# Outer loop: Iterate through each element of the array
for i in range(len(arr)):
    # Set the current index as the minimum index
    mini = i
    # Flag to track whether a swap occurred
    flag = False

    # Inner loop: Iterate through the unsorted portion of the array
    for j in range(i+1, len(arr)):
        # Check if the current element is smaller than the element at the minimum index
        if arr[j] < arr[mini]:
            # Update the minimum index
            mini = j
            # Set the flag to indicate a swap occurred
            flag = True
    
    # Check if a swap occurred in the inner loop
    if flag:
        # Swap the elements if necessary
        arr[i], arr[mini] = arr[mini], arr[i]

# Print the sorted array
print(arr)

#Selection Sort Algorithm:
#set the first unsorted element as the minimum
#for each of the unsorted elements
#     if element < currentMinimum
#       set element as new minimum
#   swap minimum with first unsorted position
# end selectionSort
