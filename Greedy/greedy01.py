import unittest


# 이것이 취업을 위한 코딩테스트다 86p
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
    for i in coins:
        count += money // i  # 몫
        money = money % i  # 나머지
    return count


# 시간 복잡도 O(k)
################################################################################


################################################################################
# 2. 큰수의 법칙 (15분걸림)
# items list중 가장 큰 수를 K번 반복하여 M번 더 하시오
def greedy02(items, M, K):
    items.sort(reverse=True)
    res = 0
    kcout = 0

    for i in range(M):
        if (K > kcout):
            res += items[0]
            kcout += 1
        else:
            res += items[1]
            kcout = 0

    return res


# 위의 방법은 M이 커질 수록 시간 초과 판정을 받을 수 있다.

def greedy02_1(items, M, K):
    items.sort(reverse=True)

    A = items[0]  # 첫번째로 큰 수
    B = items[1]  # 두번째로 큰 수

    return (M // (K + 1) * (A * K + B)) + A * (M % (K + 1))


# 반복되는 수열을 곱한다 + 이 후는 나머지 목에 대해 더 한 것
################################################################################


################################################################################

# 3. 숫자 카드 게임 (12분걸림)
# 카드 배열 n 행 m 열
# 먼저 뽑고자 하는 카드가 포함되어있는 행을 선택한다
# 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
# 따라서 처음 카드를 ㅋ골라낼 행을 선택할때 이후에 해당 행에서 가장 숫자가 낮을 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
def greedy03(nm, n, m):
    max_num = 0
    for cards in nm:
        num = min(cards)
        if num > max_num:
            max_num = num
    print(max_num)
    return max_num


################################################################################

################################################################################

# 4. 1이 될때 까지
def greedy04(n, k):
    res = True
    count = 0
    while res:
        if n == 1 :
            break
        if n % k == 0 :
            n = n / k
        else :
            n = n - 1
        count += 1

    return count


def greedy04_1(n, k):
    count = 0
    while True:
        t = (n // k) * k
        count += (n - t)
        n = t
        if n < k:
            break
        count += 1
        n = n // k

    print(count, n)
    #count += (n -1)
    return count -1


################################################################################

class GreedyTest(unittest.TestCase):
    def test_greedy01(self):
        self.assertEqual(greedy01(1260), 6)

    def test_greedy02(self):
        self.assertEqual(greedy02([2, 4, 5, 4, 6], 8, 3), 46)
        self.assertEqual(greedy02([3, 4, 3, 4, 3], 7, 2), 28)
        self.assertEqual(greedy02_1([2, 4, 5, 4, 6], 8, 3), 46)
        self.assertEqual(greedy02_1([3, 4, 3, 4, 3], 7, 2), 28)

    def test_greedy03(self):
        self.assertEqual(greedy03([[3, 1, 2], [4, 1, 4], [2, 2, 2]], 3, 3), 2)
        self.assertEqual(greedy03([[7, 3, 1, 8], [3, 3, 3, 4]], 2, 4), 3)

    def test_greedy04(self):
        self.assertEqual(greedy04(17, 4), 3)
        self.assertEqual(greedy04(25, 5), 2)
        self.assertEqual(greedy04(25, 3), 6)
        self.assertEqual(greedy04_1(17, 4), 3)
        self.assertEqual(greedy04_1(25, 5), 2)
        self.assertEqual(greedy04_1(25, 3), 6)
        self.assertEqual(greedy04_1(100, 40), 22)


if __name__ == '__main__':
    unittest.main()
