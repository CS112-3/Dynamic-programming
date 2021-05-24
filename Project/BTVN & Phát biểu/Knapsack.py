

#Tabulation
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
                                   
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

#Memoization
def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1))
        return t[n][W]