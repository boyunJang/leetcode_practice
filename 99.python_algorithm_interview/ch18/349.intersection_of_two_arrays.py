class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(nums, left, right, target):
            if left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target: return mid
                elif nums[mid] > target: return binary_search(nums, left, mid - 1, target)
                else: return binary_search(nums, mid + 1, right, target)
            else: return -1

        nums1.sort()
        nums2.sort()

        answer = []

        for i, num in enumerate(nums1):
            if i > 0 and nums1[i - 1] == num: continue
            if binary_search(nums2, 0, len(nums2) - 1, num) != -1: answer.append(num)

        return answer