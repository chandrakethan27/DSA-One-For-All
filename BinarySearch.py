# Given sorted array
arr = [1, 3, 6, 9, 99]

# Target value to find in the array
target = 9

# Initialize high and low indices for binary search
h = len(arr) - 1
l = 0

# Perform binary search
while l <= h:
    # Calculate the middle index
    mid = (l + h) // 2

    # Check if the middle element is greater than the target
    if arr[mid] > target:
        # Adjust the high index for the left half
        h = mid - 1

    # Check if the middle element is smaller than the target
    elif arr[mid] < target:
        # Adjust the low index for the right half
        l = mid + 1

    # If the middle element is equal to the target, print it and break out of the loop
    else:
        print(f"Target {target} found at index {mid}")
        break
