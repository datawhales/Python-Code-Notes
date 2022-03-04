""" Leetcode.
    22. Generate Parentheses
    Link: https://leetcode.com/problems/generate-parentheses/
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dynamic programming
        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']
        # dp[i] = ( 0 ) i-1 + ( 1 ) i-2 + ( 2 ) i-3 + .. + ( i-1 ) 0
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += (['(' + y + ')' + x for x in dp[j] for y in dp[i-j-1]])
        return dp[n]

    def generateParenthesis_2(self, n: int) -> List[str]:
        # backtracking
        string = '(' * n + ')' * n
        ret = []
        def dfs(string, path):
            # 종료 조건 및 경로 추가 조건
            if len(path) == 2 * n:
                ret.append(path)
                return
            # 개수 같은 경우 경로에 '(' 추가
            if string.count('(') == string.count(')'):
                dfs(string[1:], path + '(')
            # ')'만 남은 경우 경로에 ')' 추가
            elif '(' not in string:
                dfs(string[:-1], path + ')')
            # 경로에 '(' 추가 또는 ')' 추가
            else:
                dfs(string[1:], path + '(')
                dfs(string[:-1], path + ')')
        dfs(string, '')
        return ret

if __name__ == "__main__":
    n = 3
    answer = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    sol = Solution()
    result = sol.generateParenthesis(n)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: ["((()))", "(()())", "(())()", "()(())", "()()()"]
    result: ["((()))", "(()())", "(())()", "()(())", "()()()"]
    비교: True
    """