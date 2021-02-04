n=int(input())
a=input()
a=list(a)
r=0
for i in range(0, n):
    if a[i] == 'L':
        r+=1
if ((n+1)-(r//2))==n+1: #만약 컵홀더가 꽉찬 상황일 때, 컵홀더 하나는 사용 안함
    print(n)
else:
    print("%d" %((n+1)-(r//2)))