# from utils.math_utils import calcula_idade
#
# ano_atual = int(input('Digite o ano atual: '))
# ano_nasc = int(input('Digite o ano de nascimento: '))
#
# print("Você tem",calcula_idade(ano_atual=ano_atual, ano_nascimento=ano_nasc),"anos")





from utils.math_utils import solicitar_numero,adicao,subtracao,multiplicacao,divisao, menu_calculadora
# temperatura_celsius = receber_temperatura()
# temperatura_celsius = converter_temperatura(temperatura_celsius)
#
#
# menu_calculadora()
# solicitar_numero = solicitar_numero()
# adicao = adicao()
# subtracao = subtracao()
# multiplicacao = multiplicacao()
# divisao = divisao()



from utils.math_utils import solicita_imc

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

solicita_imc(peso, altura)
