a = int(input())
t = [500, 100, 50, 10, 5, 1]
r=0
for i in range(0, 6):
    r += (1000-a)//t[i]
    a += (t[i]*((1000-a)//t[i]))
print(r)