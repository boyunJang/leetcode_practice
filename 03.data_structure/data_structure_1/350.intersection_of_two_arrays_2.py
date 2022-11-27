from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)

        answer = []

        for key, value in dic1.items():
            if key in dic2:
                answer = answer + [key] * min(value, dic2[key])
        return answer