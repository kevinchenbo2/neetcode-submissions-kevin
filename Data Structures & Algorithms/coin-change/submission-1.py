class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [-1] * (amount + 1)
        ans[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    if ans[i - coins[j]] != -1:
                        if ans[i] == -1:
                            ans[i] = ans[i - coins[j]] + 1
                        else:
                            ans[i] = min(ans[i], ans[i - coins[j]] + 1)
        
        return ans[-1]