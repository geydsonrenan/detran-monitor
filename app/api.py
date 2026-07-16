import requests

from app.config import (
    URL,
    CPF,
    DATA_NASCIMENTO,
    COD_APTIDAO,
    TIPO_EXAME_MOTO,
    TIPO_EXAME_CARRO,
    HEADERS,
    COOKIES,
)


def consultar_datas(tipo_exame):

    params = {
        "cpf": CPF,
        "dataNascimento": DATA_NASCIMENTO,
        "codAptidao": COD_APTIDAO,
        "tipoExame": tipo_exame,
    }

    session = requests.Session()

    session.headers.update(HEADERS)

    response = session.get(URL, params=params)

    response.raise_for_status()

    return response.json()

def consultar_todas_as_datas():
    return {
        "moto": consultar_datas(TIPO_EXAME_MOTO),
        "carro": consultar_datas(TIPO_EXAME_CARRO),
    }