def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        for number in nums2:
            nums1.append(number)
        
        if len(nums1) > m + n:
            for number in nums1:
                while count != n:
                    nums1.remove(0)
                    count += 1
        nums1.sort()

merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)