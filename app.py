from datetime import timedelta, datetime
from flask import Flask, jsonify, request, render_template
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from routes import post_policial, post_responsavel, post_listarItemManutencao, get_policial,get_listarItemManutencao, get_responsavel
import os
from dotenv import load_dotenv
# gera token
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ricardo123'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/frota')
def frota():
    return render_template('frota.html')



@app.route('/listar_policial')
def listar_policial():
    var_policial = get_policial()
    return render_template('listar_policial.html',var_policial = var_policial)

@app.route('/listar_responsavel')
def listar_responsavel():
    return render_template('listar_responsavel.html')

@app.route('/listar_viatura')
def listar_viatura():
    return render_template('listar_viatura.html')

@app.route('/listar_itens')
def listar_itens():
    return render_template('listar_itens.html')


@app.route('/cadastrar_viatura')
def cadastrar_viatura():
    return render_template('cadastrar_viatura.html')

@app.route('/cadastrar_policial')
def cadastrar_policial():
    return render_template('cadastrar_policial.html')

@app.route('/cadastrar_responsavel')
def cadastrar_responsavel():
    return render_template('cadastrar_responsavel.html')

@app.route('/cadastrar_item')
def cadastrar_item():
    return render_template('cadastrar_item.html')


@app.route('/historicoManutencao')
def historicoManutencao():
    return render_template('historicoManutencao.html')


@app.route('/historicoVeiculo')
def historicoVeiculo():
    return render_template('historicoVeiculo.html')

if __name__ == '__main__':
    app.run(debug=True, port=5008,host='0.0.0.0')