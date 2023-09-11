from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para criar a tabela de tarefas se ela não existir
def create_table():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar uma tarefa
def add_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, done) VALUES (?, ?)', (task, False))
    conn.commit()
    conn.close()

# Função para listar todas as tarefas
def list_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Função para marcar uma tarefa como concluída
def mark_task_done(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET done = ? WHERE id = ?', (True, task_id))
    conn.commit()
    conn.close()


# Função para excluir uma tarefa
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    create_table()
    tasks = list_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    add_task(task)
    return redirect(url_for('index'))

@app.route('/mark_done/<int:task_id>')
def mark_done(task_id):
    mark_task_done(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        new_task = request.form['task']
        cursor.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    
    return render_template('edit.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
