import sys
import time


class Informacoes:
    def __init__(self, nome, idade, numero_conta):
        self._nome = nome.title()
        self._idade = idade
        self._numero_conta = numero_conta

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def idade(self):
        return self._idade

    @property
    def id(self):
        return self._numero_conta


class Conta(Informacoes):
    def __init__(self, nome, idade, data_aniversario, numero_conta, vitorias):
        super().__init__(nome, idade, numero_conta)
        self._data_aniversario = data_aniversario
        self.vitorias = vitorias
        self._permissao = None

    def permissao_verificar(self):
        if self._idade >= 18:
            self._permissao = True
        else:
            self._permissao = False
            print("\nPermissão negada!")
            time.sleep(5)
            sys.exit()

    def __str__(self):
        return f'Nome: {self.nome} - Vitorias: {self.vitorias}'

    @property
    def data_aniversario(self):
        return self._data_aniversario



    @property
    def permissao(self):
        return self._permissao
