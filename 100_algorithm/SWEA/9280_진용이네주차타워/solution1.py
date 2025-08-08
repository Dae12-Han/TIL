import sys
sys.stdin = open("input.txt")

from collections import deque

def if_in(i):
    for area_num in range(n):
        if parking_lot[area_num] == -1:
            if not waited:
                parking_lot[area_num] = i  # 차량 번호 기록
                car_position[i] = area_num
                return
    # 빈 공간이 없으면 대기
    waited.append(i)

def if_wait():
    for area_num in range(n):
        if parking_lot[area_num] == -1:
            priorty = waited.popleft()
            parking_lot[area_num] = priorty
            car_position[priorty] = area_num
            return

def if_out(i):
    global total_fare
    area_idx = car_position[i]
    parking_lot[area_idx] = -1  # 비움
    fee = per_fare[area_idx]
    wei = weight[i]
    total_fare += fee * wei

    if waited:
        if_wait()

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    total_fare = 0
    per_fare = [int(input()) for _ in range(n)]
    weight = [int(input()) for _ in range(m)]

    inout_log = deque()
    for _ in range(2 * m):
        inout_log.append(int(input()))

    parking_lot = [-1] * n  # -1은 빈 자리
    car_position = [-1] * m  # 각 차량이 주차된 자리 번호
    waited = deque()

    while inout_log:
        i = inout_log.popleft()
        if i > 0:
            if_in(i - 1)
        else:
            if_out(-i - 1)

    print(f"#{tc} {total_fare}")
