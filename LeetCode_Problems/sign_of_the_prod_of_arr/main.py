def arraySign(nums):
    x = 1
    for number in nums:
        x = x * number
    
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


arraySign([-1,1,-1,1,-1])