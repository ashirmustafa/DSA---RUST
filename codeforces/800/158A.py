n, k = map(int, input().split())

scores = list(map(int, input().split()))

kth_score = scores[k - 1]

count = 0
for score in scores:
    if score >= kth_score and score > 0:
        count += 1


print(count)
