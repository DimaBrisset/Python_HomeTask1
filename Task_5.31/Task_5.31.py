#.31. ���� ����������� ����� n. ����� ����� n**2+(n+1)**2+...2n**2

n=int(input("insert n: "))
s=0
for x in range(n,2*n+1):
    s+=x*x
print(s)

