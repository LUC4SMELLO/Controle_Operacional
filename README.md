<table>
  <tr>
    <td><img src="assets/images/computer_light_icon.png" width="60"></td>
    <td><h1>&nbsp;Controle Operacional &nbsp;</h1 hspace="10"></td>
    <td><img src="assets/images/computer_black_icon.png" width="60"></td>
  </tr>
</table>



Este software foi desenvolvido para ajudar a ter o controle da operação de uma empresa de forma mais simples, centralizada e eficaz. <br>

## Funcionalidades Principais:

* **`Escala`**: Permite o usuário montar a escala dos funcionários que iram trabalhar no próximo dia.
* **`Pendência & Troca`**: Permite cadastrar uma pendência ou troca de um produto para algum cliente.
* **`Relatórios`**: Contém informações da pendências e trocas feitas
* **`Relatório Entrega`**: Possibilita o usuário saber as entregas de cada caminhão e cliente.

<br>

## Tecnologias Utilizadas

- **Python 3.11.4+**
- **Tkinter 8.6**
- **Sqlite3 3.45.3+**

<br>

## Banco de Dados

- **`produtos.db`** - Comtém todos os produtos do CTA, com os seguintes campos:
    * Código Produto
    * Descrição

<br>

- **`clientes.db`** - Armazena todos os clientes da base do CTA, com os campos a seguir:
    * Código Cliente
    * Razão Social
    * Nome Fantasia
    * Cidade
    * Código Vendedor
    * Dia Semanda
    * Número Rota

<br>

- **`pendencias.db`** - Contém as informações das pendências dos clientes:
    * Número Cupom
    * Data Ocorrência
    * Carga Original
    * Código Cliente
    * Tipo
    * Responsável
    * Código Produto
    * Quantidade

<br>

- **`funcionarios.db`** - Abrange todas as informações de motoristas e ajudantes, com os seguintes campos:
    * Nome Completo
    * Função
    * CPF
    * RG

<br><br>



## Estrutura do Projeto

```
├── main.py
|
├── archives/
|   ├── Clientes Formatados.csv
|   ├── Clientes.csv
|   ├── Produtos Formatados.csv
|   ├── PRODUTOS.CSV
|
├── assets/
|   ├── icons/
|        ├── settings_dark.png
|        ├── settings_light.png
|        ├── lupa_dark.png
|        ├── lupa_light.png
|        ├── mais_dark.png
|        ├── mais_light.png
|        ├── menos_dark.png
|        ├── menos_light.png
|
├── constants/
|   ├── __init__.py
|   ├── banco_dados.py
|   ├── caminho_arquivos.py
|   ├── cores.py
|   ├── date_entry.py
|   ├── path.py
|   ├── rotas.py
|   ├── textos.py
|
├── controllers/
|   ├── __init__.py
|   |
|   ├── escala/
|   |    ├── __init__.py
|   |    ├── escala_controller.py
|   |
|   ├── menu/
|   |    ├── __init__.py
|   |    ├── menu_controller.py
|   |
|   ├── pendencia/
|   |    ├── __init__.py
|   |    ├── pendencia_controller.py
|   |
|   ├── relatorio/
|   |    ├── __init__.py
|   |    ├── relatorio_controller.py
|
|
├── database/
|   ├── __init__.py
|   ├── banco_dados_clientes.py
|   ├── banco_dados_pendencias.py
|   ├── banco_dados_produtos.py
|   ├── clientes.db
|   ├── pendencias.db
|   ├── produtos.db
|
├── models/
|   ├── __init__.py
|   |
|   ├── escala/
|   |    ├── __init__.py
|   |    ├── escala_model.py
|   |
|   ├── pendencia/
|   |    ├── __init__.py
|   |    ├── pendencia_model.py
|   |    
|   ├── relatorio/
|        ├── __init__.py
|        ├── relatorio_model.py
|
|
├── scripts/
|   ├── __init__.py
|   |
|   ├── formatar_arquivo_clientes.py
|   ├── formatar_arquivo_produtos.py
|
├── services/
|   ├── __init__.py
|   |
|   ├── clientes_service.py
|   ├── produtos_service.py
|
|
├── views/
|   ├── __init__.py
|   |
|   ├── dialogs/
|   |    ├── __init__.py
|   |    ├── exibir_mensagem.py
|   |    ├── pesquisa_cliente_view.py
|   |    ├── pesquisa_produto_view.py
|   |
|   ├── escala/
|   |    ├── components/
|   |    |    ├── __init__.py
|   |    |    ├── frame_carga.py
|   |    |
|   |    ├── editar_escala_view.py
|   |  
|   ├── menu/
|   |    ├── menu_view.py
|   |   
|   ├── pendencia/
|   |    ├── cadastrar_pendencia_view.py
|   |    ├── editar_pendencia_view.py
|   |    ├── excluir_pendencia_view.py
|   |
|   ├── relatorio/
|   |    ├── relatorio_pendencia_view.py
|   |
|   ├── janela.py
|
├── .gitignore
├── README.md
```

## Autoria
- Lucas Pereira Silva Mello

