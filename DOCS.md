# Documentação Técnica - Controle Operacional

## 1. Arquitetura e Decisões de Design
<!-- EXPLICAR ESCOLHAS DE ALTO NÍVEL -->

`Arquitetura` 

O sistema foi organizado seguindo a arquitetura MVC:

- Model: acesso ao banco de dados.
- View: responsável pela interface.
- Controller: coordena eventos da interface.

Essa arquitetura foi escolhida pela sua manutenção fácil, reutilização de código, organização.

`Banco de Dados`

Escolhi separar os bancos de dados para melhorar desempenho, escalabilidade, segurança.

## 2. Regras de Negócio Críticas
<!-- ONDE A LÓGICA "DE CABEÇA" FICA REGISTRADA -->

- Uma carga só pode ser salva se possuir número de carga.
- Relatório entrega suporta 16 cargas, caso o valor ultrapasse esse limite, uma segunda imagem é gerada.
- Um motorista só poder ter um caminhão vinculado ao seu código.
- Ao tentar excluir algum registro, os campos são "congelados", para impedir a alteração e evitar confusões.
- A data de saída da escala pega sempre o próximo dia útil, observando finais de semana e feriados.
- No diálogo para pesquisar funcionários, motoristas recebem a cor cinza, ajudantes recebem a cor branca, e funcionários já em uso ficam com a cor verde.

## 3. Guia de Integração e Dados
<!-- COMO OS DADOS EXTERNOS ENTRAM NO SISTEMA -->

`Arquivos Externos` <br> 
Arquivos que serão utilizados pelo sistema ficam localizados no diretório _**archives**_. <br>
Arquivos que são gerados pelo sistema ficam no diretório _**archives/reports/{tipo do arquivo}/**_.

`Banco Dados Clientes` <br>
O banco de dados clientes necessita do arquivo "Clientes.csv" para ser atualizado, que vem do aplicativo do CTA. O arquivo é tratado e então os clientes são inseridos se ainda não existirem ou atualizados caso já existam.

`Banco Dados Produtos` <br>
O banco de dados produtos necessita do arquivo "PRODUTOS.CSV" para ser atualizado, que vem do aplicativo do CTA. O arquivo é tratado e então os produtos são inseridos se ainda não existirem ou atualizados caso já existam.

Datas são armazenadas no formato YYYY-MM-DD.

## 4. Histórico de Decisões
<!-- EXPLICAR AS ESCOLHAS FEITAS DURANTE O PROJETO -->
`Divisão do controller da escala` <br>
Pelo crescimento do código, com quase 700 linhas, optei por dividi-lo em 4 controllers diferentes:
- **Escala Controller** - Administra as cargas de modo geral.
- **Escala Bind Controller** - Controla as binds em geral da view.
- **Escala Scroll Controller** - Coordena o scroll da view.
- **Escala Temporária Controller** - Toma conta da escala temporária, salvar, carregar, excluir.

## 5. Dificuldades
<!-- COISAS QUE LEVARAM TEMPO PARA SEREM RESOLVIDAS -->

Divisão do controller da escala, pelo fato de estar ficando grande demais.

## Autoria
- Lucas Pereira Silva Mello
