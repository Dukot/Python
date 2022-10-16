vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    print(f"Posição = {vogais.index(vogal)}, valor = {vogal}")

vogais = []

print(f"Tipo do objeto vogais = {type(vogais)}")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

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