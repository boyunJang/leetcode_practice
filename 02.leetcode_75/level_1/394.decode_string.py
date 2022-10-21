class Solution(object):
    def decodeString(self, s):
        stack = []
        num = 0
        sent = ''
        current = ''
        for c in s:
            if c == "[":
                stack.append(sent)
                stack.append(num)
                sent = ''
                num = 0
            elif c == ']':
                tmp_num = stack.pop()
                prev = stack.pop()
                sent = prev + tmp_num * sent
            elif c.isdigit():
                num = num*10 + int(c)
            else:
                sent += c
        return sent