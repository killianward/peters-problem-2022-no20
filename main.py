# Peter's Problem 2022 No.20

coins = []
sum_of_coins = 0

for i in range(1, 61):
    coins.append(1)

for i in range(1, 61, 2):
    coins[i] = 0.5

for i in range(1, 61, 3):
    coins[i] = 0.2

for i in range(1, 61, 4):
    coins[i] = 0.1

for coin in coins:
    sum_of_coins += coin

print(coins)
print(f"\nAnswer: {sum_of_coins}")
