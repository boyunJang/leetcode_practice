class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for num in nums1:
            idx = nums2.index(num)
            max_num = max(nums2[idx:])
            if num == max_num: answer.append(-1)
            else:
                for j in range(idx + 1, len(nums2)):
                    if nums2[j] > num:
                        answer.append(nums2[j])
                        break

        return answer