# Initial array to be sorted
arr = [7, 2, 5, 1, 9, 4]

# Outer loop: Iterate through each element of the array
for i in range(len(arr)):
    # Inner loop: Compare the current element with all other elements in the array
    for j in range(len(arr)):
        # Check if the current element is smaller than the element being compared
        if arr[i] < arr[j]:
            # Swap the elements if they are in the wrong order
            arr[i], arr[j] = arr[j], arr[i]

# Print the sorted array
print(arr)
