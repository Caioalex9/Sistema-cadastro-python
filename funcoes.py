import pandas as pd
import os

# Nome fixo e padronizado do arquivo
ARQUIVO = 'cadastros.csv'

def carregar_tabela():
    """Verifica se o arquivo já existe; se não, cria um modelo inicial."""
    if os.path.exists(ARQUIVO):
        tabela = pd.read_csv(ARQUIVO)
    else:
        dados = {
            'ID': [1, 2, 3],
            'Nome': ['Caio', 'Fabiano', 'Davi'],
            'Idade': [28, 24, 22],
            'Email': ['caio@gmail.com', 'fabiano@gmail.com', 'davi@gmail.com']
        }
        tabela = pd.DataFrame(dados)
        tabela.to_csv(ARQUIVO, index=False)
    return tabela


def salvar_tabela(tabela):
    """Salva a tabela no arquivo."""
    tabela.to_csv(ARQUIVO, index=False)


def gerar_id(tabela):
    """Gera o proximo ID automaticamente"""
    if tabela.empty:
        return 1
    return int(tabela['ID'].max()) + 1

def cadastrar_pessoa(tabela):
    """Faz o cadastro de uma nova pessoa com validação."""

    # Validação do nome
    while True:
        nome = str(input('Nome do novo cadastro: ')).strip().title()
        if nome == '':
            print('O nome não pode ficar em branco!')
        elif nome.isdigit():
            print('O nome não pode conter apenas números!')
        else:
            break

    # Validação da idade
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Digite apenas números para a idade!')

    # Validação do email
    while True:
        email = input('Email: ').strip().lower()
        if '@' not in email or '.' not in email:
            print('Email inválido! Digite novamente.')
        else:
            break

    novo_id = gerar_id(tabela)

    # Novo registro
    novo_dado = {
        'ID': novo_id,
        'Nome': nome,
        'Idade': idade,
        'Email': email
    }

    # Adiciona novo cadastro à tabela existente
    tabela = pd.concat([tabela, pd.DataFrame([novo_dado])], ignore_index=True)
    salvar_tabela(tabela)

    print('\nCadastro adicionado com sucesso!')
    return tabela


def listar_pessoas(tabela):
    """Mostra todos os cadastros."""
    print('~' * 26)
    print('--- LISTA DE CADASTROS --- ')
    print('~' * 26)
    print(tabela)


def menu():
    """Menu interativo do sistema."""

    tabela = carregar_tabela()

    while True:
        print('\n' + '='*30)
        print('      SISTEMA DE CADASTRO')
        print('='*30)
        print('1 - Cadastrar nova pessoa')
        print('2 - Listar todos os cadastros')
        print('3 - Sair')
        print('='*30)

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            tabela = cadastrar_pessoa(tabela)
        elif opcao == '2':
            listar_pessoas(tabela)
        elif opcao == '3':
            print('\n Encerrando o sistema ... ATÉ LOGO !')
            break

        else:
            print('Opção invalida ! Tente novamente ')
