from flask import Flask, render_template, request, redirect, session, flash, url_for
from classes import Jogo, Usuario

app = Flask(__name__)

# Adicionado criptografia
app.secret_key = "estudo"
tlt = 'Jogoteca'

jogos = []
jogos.append(Jogo('Donkey Kong','Plataforma','SNES'))
jogos.append(Jogo('Sonic', 'Plataforma', 'Genesis'))

usuario1 = Usuario('João Silva', 'joao1', 'joao1')
usuario2 = Usuario('Paulo Silva', 'paulo1', 'paulo1')
usuario3 = Usuario('Maria Silva', 'maria1', 'maria1')

usuarios = { usuario1.nick : usuario1, 
            usuario2.nick : usuario2, 
            usuario3.nick : usuario3, }

@app.route('/')
def index():

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('index'))

    return render_template('index.html', titulo = tlt, lista = jogos )


@app.route('/jogos')
def listajogos():
    
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', pagina = url_for('jogos')))
    
    return render_template('/jogos/index.html', titulo = tlt, lista = jogos )


@app.route('/jogos/cadastro')
def JogoCadastro():
    
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', pagina = url_for('JogoCadastro')))
    
    return render_template('/jogos/cadastro.html', titulo = tlt)


@app.route('/cadastrar-jogo', methods=['POST'])
def SalvarJogoNovo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jg = Jogo(nome, categoria, console)
    jogos.append(jg)
    return redirect(url_for('listajogos'))


@app.route('/deslogar', methods=['POST'])
def deslogar():
    session['usuario_logado'] = None
    return redirect(url_for('login'))


@app.route('/login')
def login():
    
    pagina_alvo = request.args.get('pagina')
    
    return render_template('login.html', titulo = tlt, pagina = pagina_alvo)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    session['usuario_logado'] = None

    print(request.form['usuario'])

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nick
            # flash(session['usuario_logado'] + ' logado com sucesso.')
            pagina_alvo = request.form['pagina']
            
            if pagina_alvo == 'None':
                return redirect(url_for('index'))
            else:
                return redirect(pagina_alvo)
        else:
            flash('Senha inválido')
            return redirect(url_for('login'))
    else:
        flash('Usuário não encontrado')
        return redirect(url_for('login'))


def VerificarUsuario():

    if 'usuario_logado' not in session or session['usuario_logado'] is None:

        return redirect(url_for('login'))


app.run(debug=True)



