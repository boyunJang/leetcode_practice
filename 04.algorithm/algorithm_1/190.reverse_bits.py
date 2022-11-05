class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        binary = []
        while n > 0:
            if n % 2 == 0: binary.append(0)
            else: binary.append(1)
            n = n // 2
        binary = binary + [0] * (32 - len(binary))
        for i in range(len(binary)):
            result *= 2
            result += binary[i]
        return result