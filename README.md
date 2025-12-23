# **Controle Operacional**

Este software foi desenvolvido para ajudar a ter o controle da operação de uma empresa de forma mais simples, centralizada e eficaz. <br>

## **Funcionalidades Principais:**

* **`Escala`**: Permite o usuário montar a escala dos funcionários que iram trabalhar no próximo dia.
* **`Pendência`**: Permite cadastrar uma pendência de um produto para algum cliente.
* **`Troca`**: Permite cadastrar uma troca de um produto para algum cliente.

## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **Tkinter 8.6**
- **Sqlite3 3.45.3+**

## **Banco de Dados**

- **`produtos.db`** - Comtém todos os produtos do CTA, com os seguintes campos:
    * Código Produto
    * Descrição
    * Unidade
    * Grupo
    * Preço Médio
    * Valor Unitário

<br>

- **`clientes.db`** - Armazena todos os clientes da base do CTA, com os campos a seguir:
    * Código Cliente
    * Razão Social
    * Rota
    * Dia de Visita
    * Código Vendedor
    * Nome Vendedor
    * Número da Rota

<br>

- **`caminhoes.db`** - Inclui todos os dados de caminhões da empresa, com os determinados campos:
    * Número do Caminhão
    * Placa do Caminhão

<br>

- **`funcionarios.db`** - Abrange todas as informações de motoristas e ajudantes, com os seguintes campos:
    * Nome Completo
    * Função
    * CPF
    * RG

<br>

- **`pendencias.db`** - Contém as informações das pendências dos clientes:
    * Número Cupom
    * Código Cliente
    * Data Ocorrência
    * Vendedor
    * Carga Original
    * Código Produto
    * Quantidade

<br>

- **`trocas.db`** - Tem as informações das trocas dos clientes:
    * Número Cupom
    * Código Cliente
    * Data Ocorrência
    * Vendedor
    * Carga Original
    * Código Produto
    * Quantidade




## **Estrutura do Projeto**

```
├── app.py
|
├── .gitignore
├── README.md
```

## **Autoria**
- Lucas Pereira Silva Mello

