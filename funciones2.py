def suma(*args, **kwargs) -> int: # *args tupla, **kargs diccionario
    """"
    Esta funcion resive .....
    """
    print(args)
    print(kwargs)
    total = 0
    for key, num in kwargs.items():
        print(f"sumando la referencia {key}")
        total += num
    return total


# print(f"El total de la suma es {suma(1, 3 , ['ldkjf', 'ldk'], num1=2, num2=5, num3=2, num4=45)}")
# # n1 = int(input())
# # n2 = int(input())
# # print(f"El total de la resta es {resta(num1=n1, num2=n2)}")


def resta(num1: int, num2: int) -> int:
    total = num1 - num2
    return total


def resta_default(num1: int = 2, num2: int = 0) -> int:
    total = num1 - num2
    return total


# print(f"El total de la resta es {resta_default(num1=5, num2=2)}")
# print(f"El total de la resta es {resta_default(num1=5)}")
# print(f"El total de la resta es {resta_default()}")

def doblar(numeros):
    numeros_copy = numeros.copy()
    print(id(numeros))
    for i, n in enumerate(numeros):
        numeros[i] *= 2


lis_n = [10, 50, 100] # {0: 10, 1: 50, 2: 100}
# print(id(lis_n))
# doblar(lis_n)
# print(lis_n)



def modify(value):
    print(id(value))
    value = value * 2 #realiza una copia del resultado
    return value


# value_start = 2
# value_modify = modify(value_start)
# print(id(value_start))
# print(value_modify)

def factoria(num):
    if num == 1:
        return 1
    return num * factoria(num - 1)  # 5 -> 5 * fac(4) -> 5 * 4 * 3 * 2 * 1


# print(factoria(100))

# 1 1 2 3 5 8 13
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)  # fib(59) + fib(58) -> fib(57) + fib(58) + fib(57) + fib(56)

print(fibo(60))






