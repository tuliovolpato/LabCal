from database import BancoDeDados
from empresas import Empresa
from equipamentos import Equipamento

def cadastrar_empresa(bancoDados):
    Empresa.cadastrar(bancoDados)

def apagar_empresa(bancoDados):
    Empresa.apagar(bancoDados)

def pesquisar_empresa(bancoDados):
    Empresa.pesquisar(bancoDados)

def cadastrar_equipamento(bancoDados):
    Equipamento.cadastrar_equipamento(bancoDados)

def apagar_equipamento(bancoDados):
    Equipamento.apagar_equipamento(bancoDados)

def pesquisar_equipamento(bancoDados):
    Equipamento.pesquisar_equipamento(bancoDados)


def menu_empresa(bancoDados):
    while True:
        print("Escolha uma opção:")
        print("1 - Cadastrar uma empresa")
        print("2 - Apagar uma empresa")
        print("3 - Pesquisar uma empresa")
        print("0 - Sair")

        sub_opcao = int(input())

        if sub_opcao == 1:
            cadastrar_empresa(bancoDados)

        elif sub_opcao == 2:
            apagar_empresa(bancoDados)

        elif sub_opcao == 3:
            pesquisar_empresa(bancoDados)

        elif sub_opcao == 0:
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_equipamento(bancoDados):
    while True:
        print("Escolha uma opção:")
        print("1 - Cadastrar um equipamento")
        print("2 - Apagar um equipamento")
        print("3 - Pesquisar um equipamento")
        print("0 - Sair")

        sub_opcao = int(input())

        if sub_opcao == 1:
            cadastrar_equipamento(bancoDados)

        elif sub_opcao == 2:
            apagar_equipamento(bancoDados)

        elif sub_opcao == 3:
            pesquisar_equipamento(bancoDados)

        elif sub_opcao == 0:
            break

        else:
            print("Opção inválida. Tente novamente.")
