def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target element is found
    return -1  # Return -1 if the target element is not found in the list

# Input: Get the list elements from the user
input_list = input("Enter a list of numbers separated by spaces: ")
arr = [int(x) for x in input_list.split()]  # Convert input strings to integers

# Input: Get the target element from the user
target = int(input("Enter the target element to search for: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")

