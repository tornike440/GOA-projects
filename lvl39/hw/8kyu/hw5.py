def square_sum(arr):
    squared_numbers = []
    for i in range(len(arr)):
        squared_numbers.append(arr[i] ** 2)
    return sum(squared_numbers)