import collections

def intersect(nums1, nums2):
        c = collections.Counter(nums1) & collections.Counter(nums2)
        ans = []
        for k, v in c.items():
            ans.extend([k] * v)
        return ans

intersect([4,9,5], [9,4,9,8,4])