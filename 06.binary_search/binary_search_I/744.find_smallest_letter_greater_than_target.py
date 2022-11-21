class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1

        answer = len(letters)

        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                answer = min(answer, mid)
                high = mid - 1
            else:
                low = mid + 1
        answer = answer % len(letters)
        return letters[answer]