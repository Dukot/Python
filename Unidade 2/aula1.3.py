vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    print(f"Posição = {vogais.index(vogal)}, valor = {vogal}")

print('----------------------------------------------------------------')

vogais = []

print(f"Tipo do objeto vogais = {type(vogais)}")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

print('----------------------------------------------------------------')
# substituímos o contador manual ("p") pela função enumerate(), que é usada para percorrer um objeto iterável retornando a posição e o valor.
for p,x in enumerate(vogais): 
    print(f"Posição = {p}, valor = {x}")

frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas)
print("abacate" in frutas)
print(min(frutas)) 
print(max(notas))
print(frutas.count("maça"))
print(frutas + notas)
print(2 * frutas)

print('----------------------------------------------------------------')

lista = ['Phyton', 30.61, "Java", 51, ['a', 'b', 20], "maça"]

print(f'Tamanho da lista = {len(lista)}')

for i, item in enumerate(lista):
    print(f"Posição = {i}, \t valor = {item} ------------> tipo individual = {type(item)}")

print("\nExemplos de slices: \n")
print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])


print('----------------------------------------------------------------')