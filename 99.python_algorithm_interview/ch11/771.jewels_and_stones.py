class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dic = {}
        for jewel in jewels:
            jewel_dic[jewel] = 1

        jewel_count = 0
        for stone in stones:
            if stone in jewel_dic:
                jewel_count += 1

        return jewel_count