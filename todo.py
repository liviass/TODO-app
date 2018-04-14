from flask import Flask, jsonify

app = Flask('todoapp')
tarefas = []

@app.route('/task')
def listar():
    return jsonify(tarefas)
