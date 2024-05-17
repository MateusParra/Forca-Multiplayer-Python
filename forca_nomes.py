import os
import random
from time import time

from conta import *
from idade_calculador import idade_calcular


def criar_conta():
    limpador()

    vitorias = 0
    criador_contas = True
    nomes = []
    contas = {}
    numeros_contas = []

    while criador_contas is True:
        nome = input("Digite seu primeiro nome: ")

        nomes = verificar_nome_existente(nome, nomes)

        valores = idade_calcular()

        idade, data_aniversario = valores[0], valores[1]

        numeros_contas, numero_conta = gerador_de_id(numeros_contas)

        contas_numero, criador_contas, contas = criando_conta(contas, nome, idade, data_aniversario, numero_conta, vitorias)
    jogar(contas)


def criando_conta(contas, nome, idade, data_aniversario, numero_conta, vitorias):
    contas_numero = len(contas) + 1

    contas["conta" + str(contas_numero)] = Conta(nome, idade, data_aniversario, numero_conta, vitorias)

    contas["conta" + str(contas_numero)].permissao_verificar()

    limpador()

    if len(contas) < 3:
        nova_conta = input("Deseja criar mais alguma conta? ").lower().strip()
    else:
        nova_conta = None

    if nova_conta == "sim" or nova_conta == "s" or nova_conta == "yes" or nova_conta == "ye":
        limpador()
        criador_contas = True
    else:
        criador_contas = False

    return contas_numero, criador_contas, contas


def gerador_de_id(numeros_contas):
    while True:
        numero_conta = random.randint(1000, 9999)

        if numero_conta not in numeros_contas:
            numeros_contas.append(numero_conta)
            break
        else:
            numero_conta = random.randint(1000, 9999)
            continue

    return numeros_contas, numero_conta


def verificar_nome_existente(nome, nomes):
    while True:
        if nome not in nomes:
            nomes.append(nome)
            break
        else:
            nome = input("Digite outro nome: ").strip().capitalize()
            continue

    return nomes


def jogar(contas):
    jogando = True
    jogador_numero = 0
    jogador = None
    while jogando is True:
        jogador_numero, jogando, jogador = placar_e_cancelador_de_loop(jogador, jogador_numero, contas, jogando)

        if jogando is False:
            break

        palavra, nome = selecionador_nomes()

        tentativas = 0

        enforcou = False
        ganhou = False
        chutes = []

        while not enforcou and not ganhou:
            
            limpador()

            print(f'Tentativa {tentativas + 1} de 7')

            desenha_forca(tentativas, palavra)

            chutes, palavra, tentativas = validador_de_letras(chutes, nome, palavra, tentativas)

            enforcou, ganhou = verificador_de_derrota_ou_vitoria(tentativas, palavra)

        if ganhou is True:
            contas["conta" + str(jogador_numero)].vitorias += 1
            vitoria()
        elif enforcou is True:
            derrota(nome)


def placar_e_cancelador_de_loop(jogador, jogador_numero, contas, jogando):
    print("\nPlacar atual: ")
    if len(contas) == 1:
        print(f"O jogador {contas["conta1"].nome} fez {contas["conta1"].vitorias} vitoria")
        jogador_numero += 1
        if jogador_numero < 2:
            vez_do_jogador(contas, jogador_numero)
        if jogador_numero > 1:
            jogando = encerrador()

    elif len(contas) == 2:
        print(
            f"{contas["conta1"].nome} = {contas["conta1"].vitorias} vitoria\n{contas["conta2"].nome} = {contas["conta2"].vitorias} vitoria")
        jogador_numero += 1
        if jogador_numero < 3:
            vez_do_jogador(contas, jogador_numero)
        if jogador_numero > 2:
            jogando = encerrador()
    else:
        print(
            f"{contas["conta1"].nome} = {contas["conta1"].vitorias} vitoria\n{contas["conta2"].nome} = {contas["conta2"].vitorias} vitoria\n{contas["conta3"].nome} = {contas["conta3"].vitorias} vitoria")
        jogador_numero += 1
        if jogador_numero < 4:
            vez_do_jogador(contas, jogador_numero)
        if jogador_numero > 3:
            jogando = encerrador()

    time.sleep(5)

    limpador()

    return jogador_numero, jogando, jogador


def vez_do_jogador(contas, jogador_numero):
    jogador = contas["conta" + str(jogador_numero)].nome
    print(f'\nVez do jogador {jogador}')


def selecionador_nomes():
    arquivo = open('nomes.txt', 'r')
    nomes = []

    for nome in arquivo:
        nomes.append(nome.strip())

    aleatorio = random.randint(0, len(nomes) - 1)
    nome = nomes[aleatorio].upper()

    arquivo.close()

    palavra = ['_' for linha in nome]

    return palavra, nome


def validador_de_letras(chutes, nome, palavra, tentativas):
    print(f'Letras chutadas:\n{' '.join(chutes)}\n')
    escolha = input("Escolha uma letra: ").strip().upper()

    index = 0

    if escolha in nome and escolha not in chutes:
        for letra in nome:
            if escolha == letra:
                palavra[index] = escolha
            index += 1
        limpador()
    else:
        print(f'Letra {escolha} não encontrada ou já existente!')
        tentativas += 1
        time.sleep(3)
        limpador()
        if tentativas == 7:
            limpador()
            desenha_forca(tentativas, palavra)
            time.sleep(3)
            limpador()

    if escolha not in chutes:
        chutes.append(escolha)

    return chutes, palavra, tentativas


def verificador_de_derrota_ou_vitoria(tentativas, palavra):
    enforcou = tentativas == 7
    ganhou = '_' not in palavra

    return enforcou, ganhou


def desenha_forca(tentativas, palavra):
    print("  _______     ")
    print(" |/      |    ")

    if tentativas == 0:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")        

    if tentativas == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if tentativas == 2:
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if tentativas == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if tentativas == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if tentativas == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print(f"_|___  {' '.join(palavra)}  ")
    print()


def vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \n")
    time.sleep(5)


def derrota(nome):
    print("Puxa, você foi enforcado!")
    print(f"O nome era {nome.capitalize()}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \n")
    time.sleep(5)


def encerrador():
    print("\nJogo encerrado!")
    jogando = False

    return jogando


def limpador():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    criar_conta()
