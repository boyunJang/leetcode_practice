class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0
        for num1 in arr1:
            new_list = [num2 for num2 in arr2 if abs(num1 - num2) <= d]
            if len(new_list) == 0: answer += 1

        return answer