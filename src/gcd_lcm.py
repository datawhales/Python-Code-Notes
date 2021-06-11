""" 두 수의 최대공약수, 최소공배수 구하는 메소드 함수 구현.
"""
def gcd(x, y):
    """ 유클리드 호제법을 이용한 최대공약수 구하는 함수.
    """
    while y > 0:
        x, y = y, x % y
    return x

def gcd_2(x, y):
    """ math 모듈 이용.
    """
    import math
    return math.gcd(x, y)

def lcm(x, y):
    return x * y // gcd(x, y)

if __name__ == "__main__":
    x, y = 24, 16
    print(f"{x}, {y}의 최대공약수: {gcd(x, y)}")
    print(f"{x}, {y}의 최소공배수: {lcm(x, y)}")
