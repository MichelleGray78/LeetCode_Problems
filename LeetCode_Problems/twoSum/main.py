def twoSum(nums, target):
        x_map = {}
        result = []
        for index, value in enumerate(nums):
            x = target - value
            if x in x_map.values():
                keys = [k for k, v in x_map.items() if v == x][0]
                result.append(keys)
                result.append(index)
            else:
                x_map.update({index:value})
        return result

twoSum(nums=[3,2,4], target=6)