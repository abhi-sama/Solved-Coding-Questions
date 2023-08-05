def maxProfit(values, weights, n, w):
    KS=[[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            KS[i][j]=max(KS[i-1][j-weights[i-1]]+values[i-1],KS[i-1][j]) if j>=weights[i-1] else KS[i-1][j]
    return KS[n][w]
    pass
