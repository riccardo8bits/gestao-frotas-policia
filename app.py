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

load_dotenv()


app = Flask(__name__)
# definir a senha, em produção colocar em local seguro
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret-change-me")
jwt = JWTManager(app)

# previne gargalo "too many connections"
"""
    ### @app.teardown_appcontext (O Zelador)
    ### Para que serve: 
    Fechar conexões de banco de dados, limpar memória temporária, fechar arquivos abertos. 
    Ele evita o temido Memory Leak (Vazamento de Memória).
    ### Curiosidade: 
    Como estamos usando o Flask-SQLAlchemy, você nunca precisará escrever esse comando na mão para o banco de dados. 
    A biblioteca já injeta um teardown_appcontext invisível no seu app que faz db.session.remove() automaticamente.
    """

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/get_policiais', methods=['GET'])
def get_policiais():
    try:
        var_policia = get_policial()
        print(var_policia)
        return render_template('listarPolicial.html', var_policia=var_policia )


    except Exception as e:
            print(f"Erro ao buscar policiais: {e}")
            return "Erro: Não foi possível listar os policiais", 500




@app.route('/get_viaturas', methods=['GET'])
def get_viaturas():
    try:

        var_viatura = get_viaturas()
        return render_template('listarViatura.html',var_viatura=var_viatura)



    except Exception as e:
        print(f"Erro ao buscar viaturas: {e}")
        return "Erro: Não foi possível listar os viaturas", 500




@app.route('/get_responsaveis', methods=['GET'])
def get_responsaveis():
    try:

        var_responsaveis = get_responsavel()
        render_template('listarResponsavel.html',var_responsaveis=var_responsaveis)


    except Exception as e:
        print(f"Erro ao buscar responsaveis: {e}")
        return "Erro: Não foi possível listar os responsaveis", 500


@app.route('/get_itens', methods=['GET'])
def get_itens():
    try:
        var_itens = get_listarItemManutencao()
        render_template('listarItemManutencao.html',var_itens=var_itens)



    except Exception as e:
        print(f"Erro ao buscar itens: {e}")
        return "Erro: Não foi possível listar os itens", 500




@app.route('/post_policial', methods=['POST'])
def rota_cadastrar_policial():
    try:

        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cargo_patente = request.form.get('cargo_patente')
        matricula = request.form.get('matricula')

 
        var_postPolicial = post_policial(nome, email, senha, cargo_patente, matricula)
        print(var_postPolicial) 

        return render_template('cadastroPolicial.html', var_postPolicial=var_postPolicial)

    except Exception as e:
        print(f"Erro ao cadastrar policial: {e}")
        return "Erro: Não foi possível cadastrar os policiais", 500


@app.route('/post_viatura', methods=['POST'])
def rota_cadastrar_viatura():
    try:

        placa = request.form.get('placa')
        ano = request.form.get('ano')
        km_atual = request.form.get('km_atual')
        prefixo = request.form.get('prefixo')
        modelo = request.form.get('modelo')
        status_atual = request.form.get('status_atual')

 
        var_postViatura = post_policial(placa, ano, km_atual, prefixo, modelo, status_atual)
        print(var_postViatura) 

        return render_template('cadastroViatura.html', var_postViatura=var_postViatura)

    except Exception as e:
        print(f"Erro ao cadastrar viatura: {e}")
        return "Erro: Não foi possível listar as viaturas", 500


@app.route('/post_responsavel', methods=['POST'])
def rota_cadastrar_responsavel():
    try:

        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cargo_funcao = request.form.get('cargo_funcao')

 
        var_postResponsavel = post_policial(nome, email, senha, cargo_funcao)
        print(var_postResponsavel) 

        return render_template('cadastroResponsavel.html', var_postResponsavel=var_postResponsavel)

    except Exception as e:
        print(f"Erro ao cadastrar responsaveis: {e}")
        return "Erro: Não foi possível cadastrar os responsaveis", 500




@app.route('/post_itens_manutencao', methods=['POST'])
def rota_itens_manutencao():
    try:

        nome_item = request.form.get('nome_item')
        descricao = request.form.get('descricao')
        categoria_falha = request.form.get('categoria_falha')
        valor_unitario = request.form.get('valor_unitario')

 
        var_postItensManutencao = post_policial(nome_item, descricao, categoria_falha, valor_unitario)
        print(var_postItensManutencao) 

        return render_template('cadastroItensManutencao.html', var_postItensManutencao=var_postItensManutencao)

    except Exception as e:
        print(f"Erro ao cadastrar policial: {e}")
        return "Erro: Não foi possível cadastrar os itens de", 500



if __name__ == '__main__':
    app.run(debug=True,port=5005,host='0.0.0.0')

