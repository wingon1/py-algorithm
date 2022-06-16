import unittest


# 기본 길찾기 문제
def example04_1(n, plans):
    # 동 북 서 남 / R D L U
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    move_type = ['R', 'D', 'L', 'U']

    x, y = 1, 1

    for plan in plans:
        for i in range(len(move_type)):
            if move_type[i] == plan:
                nx = x + dx[i]
                ny = y + dy[i]
            if nx < 1 or ny < 1 or nx > n or nx > n:
                continue
            x, y = nx, ny
    return x, y


# 모든 시각중 3이 하나라도 포함하는 경우의수 구하기
def example04_2(h):
    count = 0

    for i in range(h + 1):
        for j in range(60):
            for l in range(60):
                # 매 시각 안에 3이 포함되어있으면 카운트 증가
                if '3' in str(i) + str(j) + str(l):
                    count += 1
    return count


class MyTestCase(unittest.TestCase):
    def test_example04_1(self):
        self.assertEqual(example04_1(5, ['R', 'R', 'R', 'U', 'D', 'D']), (3, 4))

    def test_example04_2(self):
        self.assertEqual(example04_2(5), 11475)


if __name__ == '__main__':
    unittest.main()
