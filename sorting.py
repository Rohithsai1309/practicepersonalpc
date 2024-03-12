def bubble_sort(arr, n):
    # Base case: If the array has only one element or is empty, it is already sorted
    if n <= 1:
        return

    # Traverse the array and perform a pass to move the largest element to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursively call bubble_sort on the reduced array (excluding the last element)
    bubble_sort(arr, n - 1)


# Example usage
my_list = [64, 25, 12, 22, 11]
bubble_sort(my_list, len(my_list))
print(my_list)
