n, l, k=map(int, input().split())
score=0
for i in range(k):
    sub1, sub2=map(int, input().split())
    if sub2<=l:
        score+=140
    elif sub1<=l:
        score+=100
for i in range(n-k):
    sub1, sub2=map(int, input().split())
print(score)