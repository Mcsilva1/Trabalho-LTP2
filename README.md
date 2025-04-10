O código é um sistema de gerenciamento de estoque desenvolvido em Python com o banco de dados SQLite. Ele permite ao usuário cadastrar, listar, atualizar e excluir produtos por meio de um menu interativo, implementando as operações CRUD (Create, Read, Update, Delete). Abaixo está o funcionamento de cada parte: 


1. Estrutura Geral 


O programa usa o módulo sqlite3 para interagir com o banco de dados SQLite. 

O banco de dados é armazenado em um arquivo chamado estoque.db, criado automaticamente no mesmo diretório do script. 

O código é modularizado em funções específicas para conexão, criação da tabela, operações CRUD e interface do usuário. 


2. Conexão e Criação do Banco de Dados 


criar_conexao():  

Estabelece uma conexão com o banco estoque.db. 

Usa um bloco try/except para tratar erros de conexão, retornando None se falhar. 

criar_tabela():  

Executada ao iniciar o programa, cria a tabela produtos se ela não existir. 

A tabela tem os campos:  

id: Inteiro, chave primária com autoincremento. 

nome: Texto, único e obrigatório. 

quantidade: Inteiro, obrigatório. 

preco: Real (float), obrigatório. 

Usa CREATE TABLE IF NOT EXISTS para evitar sobrescrever dados existentes. 


3. Funções CRUD 


criar_produto(nome, quantidade, preco):  

Adiciona um novo produto ao banco com a query INSERT INTO produtos. 

Usa parâmetros (?) para segurança e trata erros como nomes duplicados (devido ao UNIQUE no campo nome). 

Exibe uma mensagem de sucesso ou erro. 

listar_produtos():  

Recupera todos os produtos com SELECT * FROM produtos. 

Exibe os dados em formato tabular (ID | Nome | Quantidade | Preço). 

Informa se não houver produtos cadastrados. 

atualizar_produto(id_produto, quantidade, preco):  

Atualiza quantidade e preco de um produto com base no id usando UPDATE produtos. 

Verifica se o produto existe pelo número de linhas afetadas (rowcount) e exibe o resultado. 

deletar_produto(id_produto):  

Remove um produto pelo id com DELETE FROM produtos. 

Confirma a exclusão com rowcount e informa o usuário. 


4. Menu Interativo (menu) 


Inicia chamando criar_tabela() para garantir que o banco esteja pronto. 

Apresenta um loop com 5 opções:  

Adicionar novo produto: Solicita nome, quantidade e preço. 

Listar produtos: Mostra todos os produtos cadastrados. 

Atualizar produto: Pede o ID e os novos valores. 

Deletar produto: Solicita o ID para exclusão. 

Sair: Encerra o programa. 

Usa input() para capturar escolhas e dados do usuário. 

Trata erros de entrada (ex.: valores não numéricos) com try/except, exibindo mensagens adequadas. 


5. Tratamento de Erros 


Conexão: Erros são capturados em criar_conexao() e exibidos. 

Nomes duplicados: O SQLite gera um erro de integridade, tratado em criar_produto(). 

IDs inválidos: Verificados em atualizar_produto() e deletar_produto() com rowcount. 

Entradas inválidas: Conversões para int e float no menu são protegidas por try/except. 

Fechamento da conexão: Todas as funções usam finally para fechar a conexão com conn.close(), evitando problemas de desempenho. 


6. Execução 


O programa começa com if __name__ == "__main__": menu(), iniciando o menu interativo. 

Os dados são salvos persistentemente em estoque.db, permitindo que o estoque seja mantido entre execuções. 
