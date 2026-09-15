from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ricardo123'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/frota')
def frota():
    return render_template('frota.html')


@app.route('/historicoManutencao')
def historicoManutencao():
    return render_template('historicoManutencao.html')


@app.route('/historicoVeiculo')
def historicoVeiculo():
    return render_template('historicoVeiculo.html')


@app.route('/cadastroViatura')
def cadastro_viatura():
    return render_template('cadastroViatura.html')

@app.route('/cadastroPolicial')
def cadastro_policial():
    return render_template('cadastroPolicial.html')

@app.route('/listarPolicial')
def listar_policial():
    return render_template('listarPolicial.html')

@app.route('/cadastroResponsavel')
def cadastroResponsavel():
    return render_template('cadastroResponsavel.html')

@app.route('/listarResponsavel')
def listarResponsavel():
    return render_template('listarResponsavel.html')

@app.route('/listarViatura')
def listarViatura():
    return render_template('listarViatura.html')

@app.route('/cadastroItensManutencao')
def cadastroItensManutencao():
    return render_template('cadastroItensManutencao.html')

@app.route('/listarItemManutencao')
def listarItemManutencao():
    return render_template('listarItemManutencao.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)