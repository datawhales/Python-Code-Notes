""" 광고 삽입.
    Link: https://programmers.co.kr/learn/courses/30/lessons/72414
"""
def str2num(string):
    h, m, s = string.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def num2str(num):
    h, r = divmod(num, 3600)
    m, s = divmod(r, 60)
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

def solution(play_time, adv_time, logs):
    dp = [0] * (str2num(play_time) + 1)
    log_start, log_end = [], []
    for log in logs:
        # log = "01:20:15-01:45:14"
        start, end = [str2num(t) for t in log.split('-')]
        log_start.append(start)
        log_end.append(end)
        
    for i in range(len(logs)):
        dp[log_start[i]] += 1
        dp[log_end[i]] -= 1
    for i in range(str2num(play_time)-1):
        dp[i + 1] += dp[i]
    # adv_time
    for i in range(str2num(play_time)-1):
        dp[i + 1] += dp[i]
    answer, best = 0, 0
    for i in range(str2num(play_time) - str2num(adv_time) + 1):
        if i == 0:
            tmp = dp[i + str2num(adv_time) - 1]
        else:
            tmp = dp[i + str2num(adv_time) - 1] - dp[i - 1]
        if tmp > best:
            answer, best = i, tmp
    return num2str(answer)

if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    result = "01:30:59"
    ret = solution(play_time, adv_time, logs)
    print(f"return: {ret}, result: {result}, 비교: {ret == result}")
   
    """
    return: 01:30:59, result: 01:30:59, 비교: True
    """