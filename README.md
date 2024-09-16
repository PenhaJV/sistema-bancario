# Sistema Bancário

Este é um sistema bancário simples desenvolvido em Python que permite ao usuário realizar as operações básicas de saque, depósito e consulta de extrato.

## Funcionalidades

O sistema possui as seguintes funcionalidades:
1. **Saque**: O usuário pode sacar um valor, desde que possua saldo suficiente.
2. **Depósito**: O usuário pode depositar um valor em sua conta.
3. **Extrato**: O usuário pode visualizar o saldo disponível.
4. **Sair**: O usuário pode encerrar a aplicação.

## Arquitetura

O sistema é composto pelos seguintes arquivos:

- **main.py**: O ponto de entrada da aplicação, gerencia o fluxo principal.
- **interface.py**: Contém a interface de menu para interação com o usuário.
- **manipulacao_dados.py**: Contém as funções responsáveis por realizar as operações bancárias (saque, depósito e extrato).
- **LICENSE**: Arquivo de licença MIT.
- **README.md**: Este arquivo de documentação.

## Como executar

### Pré-requisitos

- Python 3.x instalado em sua máquina.

### Passos para rodar o projeto:

1. Clone este repositório:

```bash
git clone https://github.com/PenhaJV/sistema-bancario.git
```

2. Acesse o diretório do projeto:

```bash
cd sistema-bancario
```

3. Ative o ambiente virtual (caso exista) ou instale as dependências necessárias.

4. Execute o programa:

```bash
python main.py
```

## Como funciona o código

- O arquivo `main.py` inicia o sistema bancário e apresenta um menu ao usuário, onde ele pode escolher entre sacar, depositar, visualizar o extrato ou sair.
- As opções de saque e depósito estão associadas a funções que realizam essas operações, manipulando um dicionário que armazena o saldo de um cliente fictício (`cliente1`).
- A função de extrato simplesmente exibe o saldo do cliente.

## Exemplo de Uso

```bash
Banco Seu André

1 - Sacar
2 - Depositar
3 - Extrato
4 - Sair
--------------------
> 1
insira o valor: 100

Saque efetuado

Pressione ENTER para continuar...
```

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.