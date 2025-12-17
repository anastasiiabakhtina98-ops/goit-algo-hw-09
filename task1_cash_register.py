import math 

# Маємо фіксований набір монет:
COINS = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount: int, coins=COINS) -> dict[int, int]:
    result = {}
    remaining = amount

    # жадібно беремо найбільші номінали
    for coin in sorted(coins, reverse=True):
        if remaining <= 0:
            break
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count

    # якщо набір монет дозволяє зібрати будь-яку суму, remaining буде 0
    return result


print("Для видачі взято номінал:кількість",find_coins_greedy(113))
# Результат: {50: 2, 10: 1, 2: 1, 1: 1}

# Динамічне програмування
def find_min_coins(amount: int, coins=COINS) -> dict[int, int]:
    # dp[i] — мінімальна кількість монет для суми i
    dp = [math.inf] * (amount + 1)
    # last_coin[i] — якою монетою ми "добрали" суму i
    last_coin = [-1] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for s in range(coin, amount + 1):
            if dp[s - coin] + 1 < dp[s]:
                dp[s] = dp[s - coin] + 1
                last_coin[s] = coin

    if dp[amount] == math.inf:
        # суму зібрати неможливо цими монетами
        return {}

    # відновлення набору монет
    result = {}
    s = amount
    while s > 0:
        coin = last_coin[s]
        if coin == -1:
            # на випадок помилки у даних / логіці
            break
        result[coin] = result.get(coin, 0) + 1
        s -= coin

    return dict(sorted(result.items()))  # для прикладу {1:1,2:1,10:1,50:2}


print("Для видачі взято номінал:кількість", find_min_coins(113))
# Результат: {1: 1, 2: 1, 10: 1, 50: 2}
