from flask import Flask, jsonify

app = Flask('todoapp')
tarefas = [{'id': 1, 'titulo': 'titulo', 'descricao': 'descricao da tarefa',
            'estado': False}]

@app.route('/task')
def listar():
    return jsonify(tarefas)
