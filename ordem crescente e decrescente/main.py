sequencia_numeros = str(input('Digite uma sequência de números: '))

print(f'A sequência que você digitou foi: [{sequencia_numeros}]')

lista = list(sequencia_numeros)
print('-=-'*5)
lista.sort()

print(f'Crescente: {"".join(lista)}')
print('-=-'*5)

lista.sort(reverse=True)
print(f'Decrescente: {"".join(lista)}')
print('-=-'*5)