import unittest


# 피보나치 수
# https://www.acmicpc.net/problem/2747
def baek2747():
    n = int(input())
    a = 0
    b = 1
    for i in range(n):
        a1 = b
        b = a + b
        a = a1
    return a


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(baek2747(), 55)  # add assertion here


if __name__ == '__main__':
    unittest.main()
