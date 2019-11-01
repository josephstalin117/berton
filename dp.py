import numpy as np

def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = np.zeros((n, amount+1),dtype=np.int32)
        for i in range(n):
            for j in range(amount+1):
                if coins[i] <= j:
                    dp[i, j] = max(dp[i-1, j], dp[i-1, j-coins[i]]+coins[i])
                    #print(coins[i], j, dp[j])

        for i in range(0, amount+1):
            print(dp[:, i])
        return dp[-1, -1]



coins = [1, 2, 3, 20]
res = coinChange(coins, 16)
print(res)
