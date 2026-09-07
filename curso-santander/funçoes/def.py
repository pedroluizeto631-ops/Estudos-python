def saudacao():
    print('Ola mundo !')


saudacao()

def saudacao(nome):
    print(f'Ola {nome} !')

saudacao("Alice")


def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(f'O resultado da soma é: {resultado}')

def funcao ():
    variavel_local = "Eu sou uma variável local"
    print(variavel_local)

variavel_global = "Eu sou uma variável global"

def funcao2():
    print(variavel_global)

funcao()  # Imprime 10

funcao2()  # Imprime 20

print(variavel_global)  # Imprime 20

#print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.
