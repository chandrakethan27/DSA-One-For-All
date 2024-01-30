# Initial array to be sorted
arr = [7, 2, 5, 1, 9, 4, 4]

# Outer loop: Iterate through each element of the array
for i in range(len(arr)):
    # Inner loop: Iterate through each pair of adjacent elements
    for j in range(len(arr)-1-i):
        # Compare the current element with the next element
        if arr[j] > arr[j+1]:
            # Swap the elements if they are in the wrong order
            arr[j], arr[j+1] = arr[j+1], arr[j]

# Print the sorted array
print(arr)

# Bubble Sort Logic:
# for i <- 1 to indexOfLastUnsortedElement-1
#     if leftElement > rightElement
#       swap leftElement and rightElement
# end bubbleSort
