#5.67
#????????????????? ????????? ?????????? ???: ?????? ? ?????? ????? ?????????????????? ????? 1, ?????? ????????? ????? ????? ???? ?????????? (1, 1, 2, 3, 5, 8, 13, ...). ???? ??????????? ????? n (n 3).
#?) ????? k-? ???? ?????????????????? ?????????.
#?) ???????? ?????? n ?????? ?????????????????? ?????????.
#?) ????? ??, ??? ????? ?????? n ?????? ?????????????????? ????????? ???? 
#?????? ??????

fib1 = fib2 = 1
n = int(input())
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')


fib1 = fib2 = 1
n = input("\n????? ????????: ")
n = int(n) - 2
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
print("????????:", fib2)


n = int(input("?????? ????"))
fibo = [1, 1]
[fibo.append(fibo[-2] + fibo[-1]) for i in range(n - 2)]
count = (sum(fibo))
print(fibo)
print(count)
if count % 2 == 0:
    print("??????")
else:
    print("?? ??????")

