from typing import List, Optional
#
# lista: List[int] = [1, 2, 3]  # 0, 1, 2
#
# print(lista[2])


# def div(a: int, b: int) -> float | None:
#     return a / b
#
#
# print(div(1, 3))
# print(div(1, 0))

while True:
    num1 = input("numero 1")
    num2 = input("numero 2")

    try:
        num1 = int(num1)
        num2 = int(num2)
        div = num1 / num2
        break
    except ValueError:
        print("no ingreso un numero valido, intentemolo de nuevo")
    except ZeroDivisionError:
        print("por favor ingrese un numero distiinto de zero")


print("todo salio bien")

