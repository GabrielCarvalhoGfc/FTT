# Documentação do Código Flask

Este é um exemplo de aplicativo web Flask simples para gerenciar tarefas. O aplicativo utiliza SQLite para armazenar as tarefas e fornece funcionalidades básicas, como adicionar, listar, marcar como concluídas e excluir tarefas.

## Pré-requisitos

Antes de executar este aplicativo, certifique-se de que você tenha Python e Flask instalados. Você também precisa da biblioteca SQLite para manipular o banco de dados.

```bash
pip install Flask
```
Estrutura do Código
O código é organizado em várias funções para facilitar a manutenção e a compreensão. Aqui estão as principais funções e o que elas fazem:

### create_table()
.Função que cria a tabela 'tasks' no banco de dados SQLite se ela ainda não existir. A tabela possui três colunas: 'id', 'task' e 'done'.
### add_task(task)
.Função que adiciona uma nova tarefa ao banco de dados. A tarefa é marcada como não concluída por padrão.
### list_tasks()
.Função que lista todas as tarefas existentes no banco de dados.
### mark_task_done(task_id)
.Função que marca uma tarefa como concluída com base no seu ID.
### delete_task(task_id)
.Função que exclui uma tarefa com base no seu ID.
# Rotas Flask
O aplicativo define várias rotas usando o Flask:

Rota raiz ("/"): Exibe a lista de tarefas e fornece a funcionalidade principal.
Rota "/add": Permite adicionar novas tarefas.
Rota "/mark_done/int:task_id": Permite marcar tarefas como concluídas.
Rota "/delete/int:task_id": Permite excluir tarefas.
Rota "/edit/int:task_id": Permite editar tarefas existentes.
# Executando o Aplicativo
Para executar o aplicativo, basta iniciar o script Python:
```bash python app.py ```

O aplicativo será iniciado em modo de depuração, e você poderá acessá-lo no navegador em http://127.0.0.1:5000

Certifique-se de criar a tabela de tarefas (create_table()) antes de começar a adicionar tarefas.

# Conclusão
Este é um exemplo básico de um aplicativo Flask que permite a criação e gerenciamento de tarefas. Você pode estender este aplicativo adicionando mais recursos, como autenticação de usuário, prioridades de tarefas, datas de vencimento, etc.


```Lembre-se de adaptar o nome do arquivo Python conforme necessário e incluir qualquer outra informação relevante no seu projeto. Esta documentação em formato Markdown ajudará a explicar o funcionamento do seu código Flask para outras pessoas que o utilizem ou colaborem com ele. ```
