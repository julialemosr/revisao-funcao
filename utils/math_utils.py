#exemplos
# def calcula_idade(ano_atual, ano_nascimento):
#     """
#     Calcule a idade conforme o ano de nascimento e o ano atual.
#
#     :param ano_atual: O ano atual
#     :param ano_nascimento:  O ano de nascimento
#     :return: A idade conforme o ano de nascimento.
#     """
#     idade = ano_atual - ano_nascimento
#     return idade



#1
def receber_temperatura():
    """
    Receber a temperatura em graus Celsius.
    :return: A temperatura em graus Celsius.
    """
    temperatura = int(input("Digite uma temperatura em graus Celsius:"))
    return temperatura


def converter_temperatura(temperatura_celsius):
    """
    Converter a temperatura para Kelvin e Fahrenheit.
    :param temperatura_celsius: Temperatura em graus Celsius.
    :return: Retorna a temperatura em Kelvin e Fahrenheit.
    """
    kelvin = temperatura_celsius + 273
    fahrenheit = temperatura_celsius * 1.8 + 32
    print("A temperatura em Kelvin é", kelvin)
    print("A temperatura em Fahrenheit é", fahrenheit)


#2

def solicitar_numero():
    """
    :return: Digite os 2 números para realizar a operação.
    """
    numero1 = int(input("digite um número para realizar a operação: "))
    numero2 = int(input("digite um número para realizar a operação: "))
    return numero1, numero2

def adicao(numero1, numero2):
    """
    :param número1: Digite o número que deseja
    :param numero2: Digite o número que deseja
    :return: A soma dos desses dois números.
    """
    return numero1 + numero2


def subtracao(numero1, numero2):
    """
    :param numero1: Digite o número que deseja
    :param numero2: Digite o número que deseja
    :return: A subtração desses dois números
    """
    return numero1 - numero2


def multiplicacao(numero1, numero2):
    """
    :param numero1: Digite o número que deseja
    :param numero2: Digite o número que deseja
    :return: A multiplicação desses dois números
    """
    return numero1 * numero2


def divisao(numero1, numero2):
    """
    :param numero1: Digite o número que deseja
    :param numero2: Digite o número que deseja
    :return: A divisão desses dois números
    """
    return numero1 / numero2

def menu_calculadora():
    """
    :return: Escolha a opção que deseja realizar.
    """
    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] divisão")
    print("[0] Sair")

    while True:

        escolha = input("Escolha uma das opção: ")
        if escolha == '1':
            numero1, numero2 = solicitar_numero()
            resultado = adicao(numero1, numero2)
            print(f"a soma dos números {numero1} e {numero2} é igual a {resultado}")

        elif escolha == '2':
            numero1, numero2 = solicitar_numero()
            resultado = subtracao(numero1, numero2)
            print(f"a subtração dos números {numero1} e {numero2} é igual a {resultado}")


        elif escolha == '3':
            numero1, numero2 = solicitar_numero()
            resultado = multiplicacao(numero1, numero2)
            print(f"a multiplicação dos números {numero1} e {numero2} é igual a {resultado}")



        elif escolha == '4':
            numero1, numero2 = solicitar_numero()
            resultado = divisao(numero1, numero2)
            i = 1
            while i <= 10:
                print(f"O número {numero1} dividido pelo número {numero2} é igual a {resultado}")
                i /= 1
                break

        elif escolha == '0':
            print("Fechando o programa.")
            break



#3
def solicita_imc(peso,altura):
    """
    Solicita o IMC (peso e altura).
    :param peso: O peso em Kg.
    :param altura: A altura em Kg.
    :return: Retorna o IMC.
    """
    resultado_imc = peso / (altura * altura)
    return print("seu IMC é",resultado_imc)
