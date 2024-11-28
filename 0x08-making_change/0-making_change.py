#!/usr/bin/python3
"""
Function for calculating the number of coins using dynamic programming
""" 

def makeChange(coins, total):
    """Making a change the for the numbers"""
    memo = {}

    def dp(total):
        if total < 0:
            return -1
        if total == 0:
            return 0
        
        if total in memo:
            return memo[total]

        ans = -1
        for coin in coins:
            tmp = dp(total - coin)
            if tmp != -1:
                tmp += 1
                if ans == -1:
                    ans = tmp
                else:
                    ans = min(ans, tmp)

        memo[total] = ans
        return ans

    return dp(total)
