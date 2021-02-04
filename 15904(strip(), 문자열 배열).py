voca=input().strip() #여기서 .strip()은 양쪽 문자열 끝의 공백을 지워준다 여기서는 없어도 맞았음
ucpc=["U", "C", "P", "C"]#각문자에 ""없으면 안됨 런타임 에러
idx=0
for i in voca:
    if ucpc[idx]==i:
        idx+=1
    if idx==4:
        break
print("I love UCPC" if idx==4 else "I hate UCPC")