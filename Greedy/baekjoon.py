import unittest


# ATM
# https://www.acmicpc.net/problem/11399
def baek11399(times):
    # n = int(input())
    # times = list(map(int, input().split()))
    times.sort()
    total = 0
    time = 0
    for i in times:
        time = time + i
        total += time
    return total


# 동전 0
# https://www.acmicpc.net/problem/11047
def baek11047(n, k, coin_list):
    n, k = map(int, input().split())
    coin_list = list()
    for i in range(n):
        coin_list.append(int(input()))
    coin_list.sort(reverse=True)
    count = 0
    for i in coin_list:
        if i <= k:
            a = k // i
            count += a
            k = k % i
    print(count)
    return count


class BackJoon(unittest.TestCase):
    def test_01(self):
        self.assertEqual(baek11399([3, 1, 4, 3, 2]), 32)

    def test_02(self):
        self.assertEqual(baek11047(10, 4200, [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]), 6)
        self.assertEqual(baek11047(10, 4790, [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]), 12)


if __name__ == '__main__':
    unittest.main()
