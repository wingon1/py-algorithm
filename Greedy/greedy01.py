import unittest

# 그리디 알고리즘 탐욕법 - 현재상황에서 지금 당장 좋은 것만 고르는 방법

###############################################################################
# 1. 거스름돈
# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전히 무한히 존재한다고 가정한다
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
# 힌트 - '가장 큰 화폐 단위부터' 돈을 거슬러 주는 것

def greedy01(money):
    count = 0
    coins = [500, 100, 50, 10]

    # 큰 단위 화폐부터 차례대로 확인
    for i in coins :
        count += money // i     # 몫
        money = money % i       # 나머지
    return count

# 시간 복잡도 O(k)
################################################################################

def greedy02(param):
    return param


class GreedyTest(unittest.TestCase):
    def test_greedy01(self):
        self.assertEqual(greedy01(1260), 6)  # add assertion here


if __name__ == '__main__':
    unittest.main()
