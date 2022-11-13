class Solution:
    def interpret(self, command: str) -> str:
        answer = command.replace("()", "o").replace("(al)", "al")
        return answer