 # Functions (Funções)
    # DRY - Don't repeat yourself 
    # Vários Argumentos (xargs) identificando o Parametro

# Criar uma função que armazena numers e strings(dados)

def agencia(**carro):
    return carro 

print(agencia(marca='Gol', cor='Branco', motor=1.0, placa=1234))