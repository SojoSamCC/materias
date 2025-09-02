def fib(n):

    fib_n_menos_2=0
    fib_n_menos_1=1

    for _ in range(2,n+1):
        fibo=fib_n_menos_2+fib_n_menos_1
        fib_n_menos_2 = fib_n_menos_1
        fib_n_menos_1 = fibo
    
    return fibo

# print(fib(5))

memo=[0]
vuelto = 69
denominaciones = [1,5,10,25,50]
for s in range(1,vuelto+1):
    pruebas = []
    for denom in denominaciones:
        if denom <= s:
            pruebas.append(1+memo[s-denom])
    memo.append(min(pruebas))

print(memo[vuelto])