class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak_left = [1] * len(arr)
        peak_right = [1] * len(arr)
        max_len, idx = 0, 0
        for i in range(len(arr)):
            if i > 0:
                if arr[i] > arr[i - 1]:
                    peak_left[i] = peak_left[i - 1] + 1
            if i < len(arr) - 1:
                if arr[i] > arr[i + 1]:
                    peak_right[i] = peak_right[i + 1] + 1
            tmp_len = peak_left[i] + peak_right[i]
            if tmp_len > max_len:
                max_len = tmp_len
                idx = i
        return idx