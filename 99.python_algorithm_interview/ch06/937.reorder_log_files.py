class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []

        for log in logs:
            log_split = log.split(" ")
            if "".join(log_split[1:]).isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log_split)

        letter_logs.sort(key=lambda x: x[0])

        for i in range(len(letter_logs) - 1):
            for j in range(i + 1, len(letter_logs)):
                i_log = " ".join(letter_logs[i][1:])
                j_log = " ".join(letter_logs[j][1:])
                if i_log > j_log:
                    tmp = letter_logs[i]
                    letter_logs[i] = letter_logs[j]
                    letter_logs[j] = tmp

        letter_logs = [" ".join(log) for log in letter_logs]

        return letter_logs + digit_logs