class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_list = {'(':0, '{':1, '[':2}
        close_list = {')':0, '}':1, ']':2}
        for c in s:
            if c in open_list:
                stack.append(c)
            else:
                if len(stack) == 0 or close_list[c] != open_list[stack[-1]]: return False
                stack.pop()
        if len(stack) > 0: return False
        return True