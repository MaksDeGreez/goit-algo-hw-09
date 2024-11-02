def find_coins_greedy(amount, coins):
    coins_count = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            coins_count[coin] = count
            amount -= coin * count
    return coins_count


def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_choice = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_choice[i] = coin

    if dp[amount] == float('inf'):
        return {}

    coins_count = {}
    while amount > 0:
        coin = coin_choice[amount]
        if coin in coins_count:
            coins_count[coin] += 1
        else:
            coins_count[coin] = 1
        amount -= coin

    return coins_count


def main():
    amount = 113
    coins = [50, 25, 10, 5, 2, 1]

    greedy_result = find_coins_greedy(amount, coins)
    print("Greedy algorithm result:", greedy_result)

    dp_result = find_min_coins(amount, coins)
    print("Dynamic programming result:", dp_result)

if __name__ == "__main__":
    main()
