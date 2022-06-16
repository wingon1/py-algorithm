import unittest


# 왕실의 나이트
def example04_2(point):
    x = int(ord(point[0])) - int(ord('a')) + 1
    y = int(point[1])
    # 갈수 있는 방향 총 8개
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    count = 0;
    for step in steps:
        n_x = x + step[0]
        n_y = y + step[1]
        if n_y > 0 and n_x > 0 and n_y < 9 and n_y < 9:
            count += 1
    return count


# 게임 개발
def example04_3(array):
    n, m = map(int, input().split())

    # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    d = [[0] * m for _ in range(n)]

    # 현재 캐릭터의 x, y 좌표, 방향
    x, y, direction = map(int, input().split())
    d[x][y] = 1  # 현재 좌표 방문 처리
    print(x, y, direction, d)

    # 전체 맵 정보 입력 받기
    # array = []
    # for i in range(n):
    #     array.append(list(map(int, input().split())))

    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        direction = turn_left(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 회전한 이후 정면에 바다가 아니고 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1  # 방문 처리
            x, y = nx, ny
            count += 1
            turn_time = 0
            continue
        # 회전한 이후 정면에 가보았거나 바다인 경우
        else:
            turn_time += 1
        # 4방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동
            if array[nx][ny] == 0:
                x, y = nx, ny
            # 뒤에 바다가 막혀있다면 종료
            else:
                break
            turn_time = 0
        print(count)
    return count


# 왼쪽 으로 회전
def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(example04_2('a1'), 2)
        self.assertEqual(example04_3([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]), 3)


if __name__ == '__main__':
    unittest.main()
