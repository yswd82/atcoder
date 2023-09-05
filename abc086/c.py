n = int(input())

for i in range(n):
    t, x, y = map(int, input().split(" "))

    # 時刻と総移動量の偶奇は一致する
    # 時刻より総移動量が大きいときは移動不能
    if (t + x + y) % 2 or (x + y) > t:
        print("No")
        exit()
print("Yes")
