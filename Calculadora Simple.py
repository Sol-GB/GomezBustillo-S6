operacion = input ("Ingresa una operacion (+, -, *, /)")
num1 = int(input ("ingrese el primer numero: "))
num2 = int(input ("ingrese el segundo numero: "))

if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    print(num1 / num2)
else:
    print("operacion invalida")