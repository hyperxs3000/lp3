def solve_knapsack():
    val = [50, 100, 150, 200]
    wt = [8, 16, 32, 40]
    W = 64
    n = len(val)

    # Memoization table
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)]

    def knapsack(W, i):
        # Base case
        if i < 0 or W <= 0:
            return 0

        # If already computed
        if dp[i][W] != -1:
            return dp[i][W]

        # If weight of current item > capacity, skip it
        if wt[i] > W:
            dp[i][W] = knapsack(W, i - 1)
        else:
            include = val[i] + knapsack(W - wt[i], i - 1)
            exclude = knapsack(W, i - 1)
            dp[i][W] = max(include, exclude)

        return dp[i][W]

    print("Maximum value in Knapsack =", knapsack(W, n - 1))


if __name__ == "__main__":
    solve_knapsack()
