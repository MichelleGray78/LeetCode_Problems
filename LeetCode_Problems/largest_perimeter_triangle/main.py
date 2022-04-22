def largestPerimeter(nums):
    # if a + b > c it forms a triangle
    nums.sort(reverse = True)
    for i in range(3, len(nums) + 1):
        if(nums[i-3] < nums[i -2] + nums[i - 1]):
            return sum(nums[i-3:i])

    return 0

largestPerimeter([3,2,3,4])