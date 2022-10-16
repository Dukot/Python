texto = "Aprendendo Phyton na disciplina de linguagem de programação."

print(f"Tamanho do teto = {len(texto)}")
print(f"Phyton in texto = {'Phyton' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
print(texto.upper())
print(texto.replace("a", 'e'))
print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Quantidade de palavras = {len(palavras)}")