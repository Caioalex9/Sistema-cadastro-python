# 📋 Sistema de Cadastro em Python

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## 📖 Sobre o Projet

Sistema de cadastro de pessoas desenvolvido em Python utilizando a biblioteca Pandas para manipulação e persistência de dados. O projeto faz parte do meu aprendizado no **Curso em Vídeo - Mundo 3**, onde estou aplicando conceitos de funções, validação de dados e manipulação de arquivos.

## ✨ Funcionalidades

- ✅ **Cadastro de pessoas** com validação de dados
- ✅ **Geração automática de ID** para cada cadastro
- ✅ **Validação de entrada** para nome, idade e email
- ✅ **Persistência de dados** em arquivo CSV
- ✅ **Menu interativo** para navegação
- ✅ **Listagem de cadastros** salvos

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Pandas** - Manipulação de dados
- **OS** - Gerenciamento de arquivos

## 📦 Estrutura do Projeto

```
projeto-cadastro/
│
├── main.py           # Arquivo principal (execução)
├── funcoes.py        # Funções do sistema
└── cadastros.csv     # Arquivo de dados (gerado automaticamente)
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca Pandas

### Instalação

1. Clone o repositório ou baixe os arquivos
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
==============================
      SISTEMA DE CADASTRO
==============================
1 - Cadastrar nova pessoa
2 - Listar todos os cadastros
3 - Sair
==============================
```

### Cadastro

O sistema solicita:
- **Nome**: não pode estar vazio ou conter apenas números
- **Idade**: deve ser um número válido
- **Email**: deve conter '@' e '.'

### Validações Implementadas

| Campo | Validação |
|-------|-----------|
| Nome | Não vazio, não apenas números, primeira letra maiúscula |
| Idade | Apenas números inteiros |
| Email | Deve conter '@' e '.' |
| ID | Gerado automaticamente (incremental) |

## 📊 Exemplo de Uso

```
Nome do novo cadastro: Caio Silva
Idade: 28
Email: caio@gmail.com

✅ Cadastro adicionado com sucesso!

~~~~~~~~~~~~~~~~~~~~~~~~~~
--- LISTA DE CADASTROS ---
~~~~~~~~~~~~~~~~~~~~~~~~~~
   ID      Nome  Idade              Email
0   1      Caio     28     caio@gmail.com
1   2   Fabiano     24  fabiano@gmail.com
```

## 🎯 Próximas Funcionalidades

- [ ] Adicionar campo **Sobrenome**
- [ ] Adicionar campo **CPF** com validação
- [ ] Adicionar campo **Data de Nascimento**
- [ ] Implementar função de **exclusão** de cadastros
- [ ] Implementar função de **busca** por ID
- [ ] Melhorar interface visual

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

- Manipulação de DataFrames com Pandas
- Validação de entrada de dados
- Tratamento de exceções (try/except)
- Organização de código em funções
- Persistência de dados em CSV
- Criação de menu interativo

## 👨‍💻 Autor

**Caio Alexandre**

Estudante de programação aplicando conhecimentos do Curso em Vídeo - Python (Mundo 3)

---

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

---

⭐ Se você achou este projeto interessante, considere dar uma estrela!

**Desenvolvido com 💙 e Python**
