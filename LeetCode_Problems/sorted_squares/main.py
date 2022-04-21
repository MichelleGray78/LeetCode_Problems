def sortedSquares(nums):
    squared_array = []
    
    for number in nums:
        squared_array.append(number ** 2)
    squared_array.sort()
    return squared_array