 # Functions (Funções)
    # DRY - Don't repeat yourself 
    # Vários Argumentos (xargs)

# Criar uma função que soma vários números.

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

# soma= 0 + 2 = 2+3 =5+4= 9+7= 16

x = soma(2,3,4,7)

print(x)