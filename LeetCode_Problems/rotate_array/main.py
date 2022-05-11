def rotate(nums, k):
    for i in range(k):
        nums.insert(0, nums[-1])
        del nums[-1]
        print(nums)