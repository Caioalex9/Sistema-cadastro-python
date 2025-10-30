# 📋 Sistema de Cadastro em Python

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📖 Sobre o Projeto

Sistema completo de cadastro de pessoas desenvolvido em Python utilizando a biblioteca Pandas para manipulação e persistência de dados. O projeto faz parte do meu aprendizado no **Curso em Vídeo - Mundo 3**, onde apliquei conceitos de funções, validação de dados, manipulação de arquivos e estruturas de dados.

## ✨ Funcionalidades

- ✅ **Cadastro completo** com validação de todos os campos
- ✅ **Geração automática de ID** incremental
- ✅ **Cálculo automático de idade** a partir da data de nascimento
- ✅ **Validação de CPF duplicado** no sistema
- ✅ **Consulta inteligente** por ID, nome ou sobrenome em uma única busca
- ✅ **Edição de cadastros** com opção de manter valores atuais
- ✅ **Remoção com confirmação** para evitar exclusões acidentais
- ✅ **Interface colorida** no terminal usando códigos ANSI
- ✅ **Limpeza de tela** automática entre operações
- ✅ **Menu dinâmico** e interativo
- ✅ **Persistência em CSV** utilizando Pandas

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Pandas** - Manipulação de DataFrames e persistência
- **OS** - Gerenciamento de arquivos e limpeza de tela
- **Datetime** - Cálculo de idade
- **Time** - Controle de pausas no sistema

## 📦 Estrutura do Projeto

```
Sistema-cadastro-python/
│
├── main.py           # Arquivo principal (ponto de entrada)
├── funcoes.py        # Todas as funções do sistema
├── cadastros.csv     # Arquivo de dados (gerado automaticamente)
├── README.md         # Documentação do projeto
└── .gitignore        # Arquivos ignorados pelo Git
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca Pandas

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Caioalex9/Sistema-cadastro-python.git
cd Sistema-cadastro-python
```

2. Instale a biblioteca Pandas:
```bash
pip install pandas
```

3. Execute o programa:
```bash
python main.py
```

## 💻 Como Usar

### Menu Principal

```
================================================================
                      SISTEMA DE CADASTRO
================================================================
1 - Cadastrar nova pessoa
2 - Listar todos os cadastros
3 - Consultar Pessoa
4 - Editar Cadastro
5 - Remover Pessoa
6 - Sair
================================================================
```

### Cadastro

O sistema solicita as seguintes informações:

- **Nome**: obrigatório, não pode conter apenas números
- **Sobrenome**: obrigatório, não pode conter apenas números
- **Data de Nascimento**: formato DD/MM/AAAA (idade é calculada automaticamente)
- **CPF**: formato XXX.XXX.XXX-XX (validação de duplicidade)
- **Email**: deve conter '@' e '.'

### Validações Implementadas

| Campo | Validação |
|-------|-----------|
| Nome | Não vazio, não apenas números, formato Title Case |
| Sobrenome | Não vazio, não apenas números, formato Title Case |
| Data de Nascimento | Formato DD/MM/AAAA, data válida entre 1900-2025 |
| CPF | 11 dígitos, formatação automática, validação de duplicidade |
| Idade | Calculada automaticamente a partir da data de nascimento |
| Email | Deve conter '@' e '.', formato lowercase automático |
| ID | Gerado automaticamente de forma incremental |

## 📊 Exemplo de Uso

```
Nome do novo cadastro: Paulo
Sobrenome: Soares
Data de nascimento (DD/MM/AAAA): 06/08/1988
CPF (XXX.XXX.XXX-XX): 12345678911
Idade calculada: 37 anos
Email: paulo@gmail.com

✅ Cadastro adicionado com sucesso!

================================================================
                    LISTA DE CADASTROS
================================================================
   ID   Nome Sobrenome Data_Nascimento          CPF  Idade              Email
0   1  Paulo   Soares      06/08/1988  123.456.789-11     37  paulo@gmail.com
1   2    Ana    Silva      15/03/1997  987.654.321-00     28    ana@gmail.com
```

## 🔍 Funcionalidades Detalhadas

### Consulta Inteligente
Digite ID, nome ou sobrenome e o sistema busca automaticamente:
- Se digitar número → busca por ID
- Se digitar texto → busca por nome ou sobrenome

### Edição de Cadastros
- Mostra dados atuais da pessoa
- Permite editar cada campo individualmente
- Deixar em branco mantém o valor atual
- Recalcula idade automaticamente ao alterar data de nascimento

### Remoção Segura
- Mostra os dados antes de remover
- Solicita confirmação (S/N)
- Opção de cancelar a qualquer momento

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

- Manipulação avançada de DataFrames com Pandas
- Validação robusta de entrada de dados
- Tratamento completo de exceções (try/except)
- Modularização de código em funções reutilizáveis
- Persistência de dados em formato CSV
- Criação de interfaces interativas no terminal
- Uso de cores ANSI para melhor UX
- Cálculo de datas com datetime
- Boas práticas de versionamento com Git
- Documentação de código com docstrings

## 🎯 Conceitos Aplicados

- ✅ Funções e modularização
- ✅ Estruturas de repetição (while, for)
- ✅ Estruturas condicionais
- ✅ Manipulação de strings
- ✅ Listas e dicionários
- ✅ Tratamento de exceções
- ✅ Trabalho com arquivos
- ✅ Bibliotecas externas (Pandas)
- ✅ Validação de dados
- ✅ Formatação de saída

## 👨‍💻 Autor

**Caio Alexandre**

Estudante de programação aplicando conhecimentos do Curso em Vídeo - Python (Mundo 3)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue)](https://www.linkedin.com/in/caioalex9)
[![GitHub](https://img.shields.io/badge/GitHub-Seguir-black)](https://github.com/Caioalex9)

---

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e está disponível sob licença livre para estudo.

---

## 🤝 Contribuições

Sugestões e feedback são sempre bem-vindos! Sinta-se à vontade para:
- Abrir uma issue
- Fazer um fork do projeto
- Sugerir melhorias

---

⭐ **Se este projeto te ajudou de alguma forma, considere dar uma estrela!**

**Desenvolvido com 💙 e Python**
