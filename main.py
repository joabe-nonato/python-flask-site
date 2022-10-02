from flask import Flask, render_template, request, redirect
from classes import Jogo

app = Flask(__name__)

tlt = 'Site em Flask'
jogos = []

jogos.append(Jogo('Donkey Kong','Plataforma','SNES'))
jogos.append(Jogo('Sonic', 'Plataforma', 'Genesis'))

@app.route('/')
def index():
    return render_template('index.html', titulo = tlt, lista = jogos )

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo = tlt)

@app.route('/create', methods=['POST'])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jg = Jogo(nome, categoria, console)
    jogos.append(jg)
    # return render_template('index.html', titulo = tlt, lista = jogos )
    return redirect('/')

app.run(debug=True)
