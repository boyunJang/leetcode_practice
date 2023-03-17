class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        num_of_bytes = -1

        for num in data:
            # print(bin(num)[2:].zfill(8), num_of_bytes)
            tmp = bin(num)[2:].zfill(8)
            if num_of_bytes != -1:
                if tmp[:2] != "10": return False
                num_of_bytes -= 1
            else:
                if tmp[0] == "0":
                    continue
                else:
                    if tmp[:5] == "11110":
                        num_of_bytes = 2
                    elif tmp[:4] == "1110":
                        num_of_bytes = 1
                    elif tmp[:3] == "110":
                        num_of_bytes = 0
                    else:
                        return False
        if num_of_bytes == -1: return True
        return False