n = int(input())
count = 0

coins = [500, 100, 50, 10, 5, 1]
change = 1000 - n

for coin in coins:
    count += change//coin
    change %= coin

print(count)