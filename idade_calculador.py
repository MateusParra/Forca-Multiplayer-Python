import datetime
import sys


def idade_calcular():
    data_atual = datetime.datetime.now()

    aniversario_dia = int(input("\nQual o dia do seu aniversário? "))
    aniversario_mes = int(input("\nQual o mes do seu aniversário? "))
    aniversario_ano = int(input("\nQual o ano do seu aniversário? "))

    requisitor_idade_dia = data_atual.day - aniversario_dia
    requisitor_idade_mes = data_atual.month - aniversario_mes
    requisitor_idade_ano = data_atual.year - aniversario_ano

    data_aniversario = calcular_data_aniversario(aniversario_dia, aniversario_mes, aniversario_ano)

    if requisitor_idade_mes == 0 and requisitor_idade_dia >= 0 or requisitor_idade_mes > 0:
        idade = requisitor_idade_ano
    else:
        idade = requisitor_idade_ano - 1

    if idade > 100 or idade < 0:
        print("\nIdade inválida!")
        sys.exit()

    return idade, data_aniversario, aniversario_dia, aniversario_mes, aniversario_ano, data_aniversario


def calcular_data_aniversario(dia, mes, ano):
    dia = str(dia)
    mes = str(mes)
    ano = str(ano)
    data_aniversario = dia + "/" + mes + "/" + ano
    return data_aniversario
