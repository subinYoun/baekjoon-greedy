n = int(input())
for i in range((n//5), -1, -1):
    if ((n - (5*i)) % 3) == 0:
        print("%d" %(i+(n - (5*i))//3))
        break
    elif i == 0:
        print("-1")