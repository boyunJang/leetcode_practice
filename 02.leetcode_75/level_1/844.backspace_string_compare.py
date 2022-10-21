class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for c in s:
            if c == "#" and len(s_stack) > 0:
                s_stack.pop()
            elif c != "#":
                s_stack.append(c)
        for c in t:
            if c == "#" and len(t_stack) > 0:
                t_stack.pop()
            elif c != "#":
                t_stack.append(c)
        if s_stack == t_stack: return True
        else: return False