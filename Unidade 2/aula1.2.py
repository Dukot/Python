texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""

print(f"Tamanho do texto = {len(texto)}")

texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")

lista_palavras = texto.split()

print(f"tamanho da lista = {len(lista_palavras)} ")

total = lista_palavras.count("string")+lista_palavras.count("strings")

print(f"Quantidade de vezes que string ou strings aparecem = {total} ")