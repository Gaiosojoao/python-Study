# Functions (Funções)
    # DRY - Don't repeat yourself 
# Parametro --> Argumento
# Default = Aquele que você define o valor no parametro
# Non-Default = Aquele que você não define o vaLor no parametro

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 5 )
boas_vindas('Ronaldo', 5 )
boas_vindas('Linda', 5 )
boas_vindas('Hellen Beatriz', 8 )



