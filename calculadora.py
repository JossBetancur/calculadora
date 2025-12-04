# calculadora.py
#Version mejorada
# Script básico para operaciones matemáticas
numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == '+':
    print("Resultado:", numero_1 + numero_2)

elif operacion == '-':
    print("Resultado:", numero_1 - numero_2)

elif operacion == '*':
    print("Resultado:", numero_1 * numero_2)

elif operacion == '/':
    if numero_2 != 0:
        print("Resultado de la operacion:", numero_1 / numero_2)
    else:
        print("Error: no se puede dividir por cero.")
else:
    print("Operacion no valida.")
