n = int(input("Informe um número: "))

# Dois primeiros números da sequência de Fibonacci
a = 0
b = 1

# A assume o valor de b, e b assume o valor da soma de a e b, fazendo com que a sequência avance até chegar no valor n informado
while b < n:
    a, b = b, a + b

if b == n or n == 0:
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")
