""" 00:00:00 형태의 타임스탬프를 연속적인 숫자로 변환하는 함수.
    HH:MM:SS 형태.
    Hour는 00 ~ 99.
    Minute은 00 ~ 59.
    Second는 00 ~ 59.
"""
def ts2num(ts):
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def num2ts(num):
    m, s = divmod(num, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

if __name__ == "__main__":
    ts = "01:14:35"
    print(ts)
    print('num:', ts2num(ts))
    num = ts2num(ts)
    print('ts:', num2ts(num))