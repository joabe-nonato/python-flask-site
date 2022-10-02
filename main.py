from flask import Flask, render_template, request, redirect, session, flash
from classes import Jogo

app = Flask(__name__)

# Adicionado criptografia
app.secret_key = "estudo"

tlt = 'Jogoteca'
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

@app.route('/login')
def login():
    return render_template('login.html', titulo = tlt)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    session['usuario_logado'] = ''

    if request.form['senha'] == '123':
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso.')
        return redirect('/')
    else:
        flash('Login ou senha inválido')
        return redirect('/login')

app.run(debug=True)
