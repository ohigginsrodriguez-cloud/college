def fibo(n):

    if len(fibo_list) == n:
        for _ in fibo_list:
            print(_)
        return

    num = a + b
    fibo_list.append(num)

    return fibo()


# n = int(input("Teclea la cantidad de numeros fibonacci: "))
a, b = 0, 1
fibo_list = []
fibo(5)
