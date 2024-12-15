#!/usr/bin/python3
# Coding some of the prime game logic here


def isWinner(x, nums):
    maximumNum = max(nums)
    sieve = [True for _ in range(maximumNum + 1)]
    prefix_sum = [0 for _ in range(maximumNum + 1)]

    sieve[0] = sieve[1] = False
    for number in range(2, maximumNum + 1):
        if sieve[number]:
            j = number ** 2
            prefix_sum[number] = 1
            while j < maximumNum + 1:
                sieve[j] = False
                j += number
        prefix_sum[number] += prefix_sum[number - 1]
    
    Maria = 0
    Ben = 0
    for index in range(len(nums)):
        if prefix_sum[nums[index]] % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Ben > Maria:
        return "Ben"
    elif Maria > Ben:
        return "Maria"
    else:
        return None


