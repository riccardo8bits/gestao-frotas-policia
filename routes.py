import requests 

endereco = "http://10.135.232.19:5005"

def get_policial():
    url = f"{endereco}/get_policiais"

    result_policia = requests.get(url)

    return result_policia.json()

def post_policial(nome,email,senha,cargo_patente,matricula):
    url = f"{endereco}/post_policial"

    dados = {
        "nome": nome,
        "email": email,
        "senha": senha, 
        "cargo_patente": cargo_patente, 
        "matricula": matricula
    }

    result_policia = requests.post(url=url, json=dados)

    return result_policia.json()


    