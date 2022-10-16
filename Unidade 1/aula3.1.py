def imprimir_mensagem(disciplina, curso):
    return(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}")

imprimir_mensagem("Python", "Engenharia de Software")    
mensagem = imprimir_mensagem("Python", "Engenharia de Software")
print(mensagem)

def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m)-1] #O mês 1, estará na posição 0!
    return f'{d} de {mes_extenso} de {a}' 
print(converter_mes_para_extenso('10/05/2021'))