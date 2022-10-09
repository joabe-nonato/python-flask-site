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
    VerificarUsuario()
    return render_template('index.html', titulo = tlt, lista = jogos )


@app.route('/jogos')
def listajogos():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')
    return render_template('/jogos/index.html', titulo = tlt, lista = jogos )


@app.route('/jogos/cadastro')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')
    return render_template('/jogos/cadastro.html', titulo = tlt)


@app.route('/cadastrar-jogo', methods=['POST'])
def cadastrarjogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jg = Jogo(nome, categoria, console)
    jogos.append(jg)
    return redirect('/jogos')


@app.route('/deslogar', methods=['POST'])
def deslogar():
    session['usuario_logado'] = None
    return redirect('/login')


@app.route('/login')
def login():
    return render_template('login.html', titulo = tlt)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    session['usuario_logado'] = None

    if request.form['senha'] == '123':
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso.')
        return redirect('/')
    else:
        flash('Login ou senha inválido')
        return redirect('/login')


def VerificarUsuario():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')


app.run(debug=True)



