import pandas as pd
import os
from time import sleep

def linha(tam = 64):
    print('-'*tam)

def cabeçalho(txt):
    linha()
    print(f'{txt.center(64)}')
    linha()

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Nome fixo e padronizado do arquivo
ARQUIVO = 'cadastros.csv'

def carregar_tabela():
    """Verifica se o arquivo já existe; se não, cria um modelo inicial."""
    if os.path.exists(ARQUIVO):
        tabela = pd.read_csv(ARQUIVO)
    else:
        # Cria estrutura vazia com as colunas corretas
        tabela = pd.DataFrame(columns=['ID', 'Nome','Sobrenome', 'Data_Nascimento', 'CPF', 'Idade', 'Email'])
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
            print('\033[0;31mO nome não pode ficar em branco!\033[m')
        elif nome.isdigit():
            print('\033[0;31mO nome não pode conter apenas números!\033[m')
        else:
            break
    
    while True:
        sobrenome = str(input('Sobrenome: ')).strip().title()

        if sobrenome == '':
            print('\033[0;31mERRO ! Insira seu sobrenome \033[m')
        
        elif sobrenome.isdigit():
            print('\033[0;31mERRO ! O sobrenome não pode conter digitos !\033[m')
        else:
            break
    
    data_nascimento = validar_data_nascimento()

    cpf = validar_cpf()

    #valida se CPF ja esta cadastrado 
    if not tabela.empty and cpf in tabela['CPF'].values:
        print('\033[0;31mERRO ! Este CPF já está cadastrado no sistema.\033[m')
        return tabela

    # Validação da idade
    idade = calcular_idade(data_nascimento)
    print(f'Idade calculada: {idade} anos')

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
        'Sobrenome': sobrenome,
        'Data_Nascimento': data_nascimento,
        'CPF': cpf,
        'Idade': idade,
        'Email': email
    }

    # Adiciona novo cadastro à tabela existente
    tabela = pd.concat([tabela, pd.DataFrame([novo_dado])], ignore_index=True)
    salvar_tabela(tabela)

    print('\n\033[0;32mCadastro adicionado com sucesso!\033[m')
    return tabela


def listar_pessoas(tabela):
    """Mostra todos os cadastros."""
    cabeçalho('LISTA DE CADASTROS')

    if tabela.empty:
        print('\n Nenhum cadastro encontrado ! A lista está vazia.')
    
    else:

        print(tabela)


def menu():
    """Menu interativo do sistema."""

    tabela = carregar_tabela()

    while True:
        limpar_tela()
        cabeçalho('SISTEMA DE CADASTRO')
        mainmenu = ['Cadastrar nova pessoa', 'Listar todos cadastros', 'Consultar Pessoa','Editar Cadastro','Remover Pessoa','Sair']
        c = 1
        for item in (mainmenu):
            print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
            c += 1


        linha()

        opcao = input('\033[0;33mEscolha uma opção: \033[m').strip()

        if opcao == '1':
            tabela = cadastrar_pessoa(tabela)
        elif opcao == '2':
            listar_pessoas(tabela)
        elif opcao == '3':
            consultar_pessoa(tabela)
        elif opcao == '4':
            tabela = editar_cadastro(tabela)
        elif opcao == '5':
            tabela = remover_pessoa(tabela)
        elif opcao == '6':
            print('\n Encerrando o sistema ... ATÉ LOGO !')
            break

        else:
            print('\033[0;31mOpção invalida ! Tente novamente \033[m')

        input('\n\033[0;33mPressione ENTER para continuar...\033[m')   
        sleep(3)

def remover_pessoa(tabela):
    """Remove pessoa da tabela pelo ID"""

    if tabela.empty:
        print('\nNão há cadastro para remover')
        return tabela

    cabeçalho('CADASTRO DISPONIVEIS')
    print(tabela[['ID', 'Nome', 'Email']])

    while True:
        try:
            id_remover = int(input('\nDigite o ID para remoção:(0 para ENCERRAR) '))


            if id_remover == 0:
                print('\033[0;31mOperação cancelada\033[m')
                break

        
            #verifica se o id existe
            if id_remover not in tabela['ID'].values:
                print(f'\n\033[0;31m{id_remover} não encontrado ! Tente novamente.\033[m')
                continue

            #mostra quem será removido
            pessoa = tabela[tabela['ID'] == id_remover]
            print(pessoa[['ID', 'Nome', 'Idade', 'Email']])
            print('encontrada para removoção.')

            confirma = str(input(f'\nTem certeza que deseja remover(S/N):')).strip().upper()

            if confirma == 'S':
                #remove pessoa
                tabela = tabela[tabela['ID'] != id_remover].reset_index(drop=True)
                salvar_tabela(tabela)
                print('Cadastro removido com sucesso !')
            
            else:
                print('\033[0;31mCancelando ação !\033[m')

            return tabela
        
        except (ValueError,TypeError):
            print('\033[0;31mERRO ! Digite apenas numeros inteiros validos.\033[m')

        except(KeyboardInterrupt):
            print('\033[0;31mOperação cancelada ! O usuario prefiriu não digitar\033[m')
            break

def calcular_idade(data_nascimento):
    """Calcula a idade a partir da data de nascimento"""
    from datetime import datetime

    dia, mes, ano = map(int, data_nascimento.split('/'))
    nascimento = datetime(ano, mes, dia)
    hoje = datetime.now()

    idade = hoje.year - nascimento.year

    #valida se ja fez aniversario
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    return idade



def validar_data_nascimento():
    """Valida a data de nascimento por DD/MM/AAAA"""

    while True:
        data = input('Data de nascimento (DD/MM/AAAA): ').strip()

        if len(data) != 10 or data[2] != '/' or data[5] != '/':
            print('Formato invalido ! Use DD/MM/AAAA (ex: 15/05/1997)')
            continue

        try: 
            dia, mes, ano = data.split('/')
            dia, mes, ano = int(dia), int(mes), int(ano)

            #verificação

            if not (1 <= dia <= 31):
                print('Dia invalido ! Digite um valor entre 1 e 31 ')
                continue

            if not (1 <= mes <= 12):
                print('Mes invalido ! Digite um valor entre 1 e 12')
                continue
            if not (1900 <= ano <= 2025):
                print('Ano invalido ! Digite um valor entre 1900 e 2025')
                continue

            return data

        except ValueError:
            print('\033[0;31mData invalida ! Use apenas numeros \033[m')


def validar_cpf():
    """Valida CPF (formato basico: XXX.XXX.XXX-XX)"""

    while True:
        
        cpf = input('CPF (XXX.XXX.XXX-XX): ')

        #validação sem pontos ou traços
        cpf_numeros = cpf.replace('.', '').replace('-', '')

        #verifica digitos
        if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
            print('\033[0;31mCPF INVALIDO ! Deve conter 11 números.\033[m')
            continue

        #formatação
        cpf_formatado= f'{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}'

        return cpf_formatado

def consultar_pessoa(tabela):
    """Busca pessoa por nome"""
    
    if tabela.empty:
        print('\n Não há cadastros para consultar!')
        return
    
    cabeçalho('CONSULTAR PESSOA')
    busca = input('Digite o ID, nome ou sobrenome: ').strip()
    
    # Busca por id, nome ou sobrenome
    if busca.isdigit():
        id_busca = int(busca)

        if id_busca in tabela['ID'].values:
            resultado = tabela[tabela['ID'] == id_busca]
            print(f'\n\033[0;32m Pessoa encontrada:\033[m\n')
            print(resultado)
            return
        else:
            print(f'\n\033[0;31m ID {id_busca} não encontrado!\033[m')
            return
    

    # Se não for número, busca por nome/sobrenome
    busca_texto = busca.title()
    resultado = tabela[
        tabela['Nome'].str.contains(busca_texto, case=False, na=False) | 
        tabela['Sobrenome'].str.contains(busca_texto, case=False, na=False)
    ]
    
    if resultado.empty:
        print(f'\n\033[0;31m Nenhuma pessoa encontrada com "{busca}".\033[m')
    else:
        print(f'\n\033[0;32m Encontrado(s) {len(resultado)} resultado(s):\033[m\n')
        print(resultado)


def editar_cadastro(tabela):
    """Edita um cadastro existente"""
    
    if tabela.empty:
        print('\n\033[0;31m Não há cadastros para editar!\033[m')
        return tabela
    
    cabeçalho('EDITAR CADASTRO')
    print(tabela[['ID', 'Nome', 'Sobrenome', 'Email']])
    
    try:
        id_editar = int(input('\nDigite o ID para editar (0 para cancelar): '))
        
        if id_editar == 0:
            print('\033[0;31mOperação cancelada\033[m')
            return tabela
        
        if id_editar not in tabela['ID'].values:
            print(f'\n\033[0;31m{id_editar} não encontrado!\033[m')
            return tabela
        
        # Mostra dados atuais
        pessoa = tabela[tabela['ID'] == id_editar]
        print('\n Dados atuais:')
        print(pessoa)
        
        print('\n\033[0;33m Deixe em branco para manter o valor atual\033[m')
        linha()
        
        # Pega o índice real da linha
        idx = tabela[tabela['ID'] == id_editar].index[0]
        
        # Nome
        novo_nome = input(f"Novo nome [{pessoa['Nome'].values[0]}]: ").strip().title()
        if novo_nome:
            tabela.at[idx, 'Nome'] = novo_nome
        
        # Sobrenome
        novo_sobrenome = input(f"Novo sobrenome [{pessoa['Sobrenome'].values[0]}]: ").strip().title()
        if novo_sobrenome:
            tabela.at[idx, 'Sobrenome'] = novo_sobrenome
        
        # Data de nascimento (recalcula idade)
        nova_data = input(f"Nova data nascimento [{pessoa['Data_Nascimento'].values[0]}] (DD/MM/AAAA): ").strip()
        if nova_data and len(nova_data) == 10:
            try:
                # Valida a data
                dia, mes, ano = map(int, nova_data.split('/'))
                if (1 <= dia <= 31) and (1 <= mes <= 12) and (1900 <= ano <= 2025):
                    tabela.at[idx, 'Data_Nascimento'] = nova_data
                    tabela.at[idx, 'Idade'] = calcular_idade(nova_data)
                    print(f'\033[0;32m Idade recalculada: {tabela.at[idx, "Idade"]} anos\033[m')
                else:
                    print('\033[0;31m Data inválida! Mantendo valor anterior.\033[m')
            except:
                print('\033[0;31m Formato inválido! Mantendo valor anterior.\033[m')
        
        # Email
        novo_email = input(f"Novo email [{pessoa['Email'].values[0]}]: ").strip().lower()
        if novo_email and ('@' in novo_email and '.' in novo_email):
            tabela.at[idx, 'Email'] = novo_email
        elif novo_email:
            print('\033[0;31m Email inválido! Mantendo valor anterior.\033[m')
        
        salvar_tabela(tabela)
        print('\n\033[0;32m Cadastro atualizado com sucesso!\033[m')
        
    except ValueError:
        print('\033[0;31mERRO! Digite apenas números para o ID.\033[m')
    
    return tabela