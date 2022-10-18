# Para calcularmos o nosso IMC, precisamos dividir o nosso peso (em kg) pela altura ao quadrado (em metros)
# Vamos precisar de 3 variáveis

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / altura ** 2 # Podemos também usar a expressão {peso / (pow(altura, 2))}

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print('Peso normal')    
elif 25 <= imc < 29.9:
    print('Sobrepeso')    
elif 30 <= imc < 34.9:
    print('Obesidade Grau I')
elif 35 <= imc < 39.9:
    print('Obesidade grau II')    
else:
    print('Obesidade Grau III ou Mórbida')    

print(f'Seu imc é {imc:.2f}')