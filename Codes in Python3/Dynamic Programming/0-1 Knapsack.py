from os import *
from sys import *
from collections import *
from math import *
def knapsack(weights, values, n, W):
    # Initialize the DP array for the previous row with 0 values
    prev = [0] * (W + 1)

    # Base case initialization: for the first item
    for i in range(weights[0], W + 1):
        prev[i] = values[0]

    # Iterate through all items
    for ind in range(1, n):
        # To avoid overwriting values we still need to read, iterate backwards
        for weight in range(W, weights[ind] - 1, -1):
            # If including the item is possible, and yields a better value, include it
            prev[weight] = max(prev[weight], values[ind] + prev[weight - weights[ind]])

    # The last element in 'prev' now represents the maximum value achievable
    return prev[W]

# Read input as specified in the question
T = int(input())  # Read number of test cases

for _ in range(T):
    N = int(input())  # Number of items
    weights = list(map(int, input().split()))  # Weights of the items
    values = list(map(int, input().split()))  # Values of the items
    W = int(input())  # Maximum weight of the knapsack

    # Call the knapsack function and print the result
    print(knapsack(weights, values, N, W))


# def maxProfit(values, weights, n, w):
#     KS=[[0] * (w + 1) for _ in range(n + 1)]
#     for i in range(1,n+1):
#         for j in range(1,w+1):
#             KS[i][j]=max(KS[i-1][j-weights[i-1]]+values[i-1],KS[i-1][j]) if j>=weights[i-1] else KS[i-1][j]
#     return KS[n][w]
#     pass
