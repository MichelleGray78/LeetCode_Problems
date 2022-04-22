def moveZeroes(nums): 
        zeroes = []
        while 0 in nums:
            nums.remove(0)
            zeroes.append(0)
        
        while 0 in zeroes:
            zeroes.remove(0)
            nums.append(0)