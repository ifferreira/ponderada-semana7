from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB
from flask_cors import CORS
from datetime import datetime
import robot

#Cria a instância do Flask no App
app = Flask(__name__)

#Cria um banco de dados tinydb
db = TinyDB('banco.json')

CORS(app)

#Rota de teste
@app.route('/')
def ola():
    return render_template('index.html')

#Rota para redirecionar para index
@app.route('/redirect_index')
def redirect_index():
    return redirect(url_for('index'))

#Rota para redirecionar para logs
@app.route('/redirect_logs')
def redirect_logs():
    return redirect(url_for('logs'))

#Rota de logs
@app.route('/logs')
def logs():
    return render_template('logs.html')

#Rota para listar logs
@app.route('/get_logs')
def get_logs():
    a = ""
    for log in db.all():
        a += f'{log["date"]} - {log["message"]}<br>'
    return a


#Rota para definir posição absoluta do robô
@app.route('/definir_posicao', methods=['POST'])
def definir_posicao():
    position_X = request.form['position_X']
    position_Y = request.form['position_Y']
    position_Z = request.form['position_Z']
    robot.definir_posicao(float(position_X), float(position_Y), float(position_Z))
    db.insert({'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'position_X': float(position_X), 'position_Y': float(position_Y), 'position_Z': float(position_Z), 'message': f'Posição do robô definida para ({position_X}, {position_Y}, {position_Z})'})
    return f'Posição do robô definida para ({position_X}, {position_Y}, {position_Z})'

#Rota para definir posição home do robô
@app.route('/definir_home')
def definir_home():
    robot.definir_posicao(250, 0, 150.00)
    db.insert({'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'position_X': 243.84, 'position_Y': 5.12, 'position_Z': 157.94, 'message': 'Posição do robô definida para HOME'})
    return 'Posição do robô definida para HOME'


if __name__ == '__main__':
    app.run(host='localhost', port=8000)

