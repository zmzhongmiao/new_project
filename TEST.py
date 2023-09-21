import math
def is_su(n):
    if n==1 or n == 2:
        return True
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:
            return False
    return True

cnt = 0
sum=0
for i in range(1,1000):
    if is_su(i):
        cnt+=1
        sum += i
        print(i)
print(cnt, '', sum)
