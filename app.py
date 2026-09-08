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





    




if __name__ == '__main__':
    app.run(debug=True)