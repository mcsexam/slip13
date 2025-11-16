import math

def minimax(depth, nodeIndex, isMax, scores, h):
    if depth == h:
        return scores[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, h),  
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, h)  
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, h), 
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, h) 
        )

scores = [3, 5, 2, 9]

h = int(math.log(len(scores), 2))

res = minimax(0, 0, True, scores, h)

print("The optimal value is:", res)
