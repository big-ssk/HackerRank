# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product


def fun(k, m):
    arrs = [[x * x for x in map(int, input().split()[1:])] for _ in range(k)]
    return max([sum(i for i in x) % m for x in product(*arrs)])


k, m = map(int, input().split())
print(fun(k, m))
