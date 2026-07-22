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
        "cpf": f'{CPF}',
        "dataNascimento": f'{DATA_NASCIMENTO}',
        "codAptidao": f'{COD_APTIDAO}',
        "tipoExame": f'{tipo_exame}',
    }

    session = requests.Session()

    session.headers.update(HEADERS)
    session.cookies.update(COOKIES)

    response = session.get(
        URL,
        params=params,
        timeout=60
    )

    resposta_texto = response.text.strip()

    response.raise_for_status()
    if resposta_texto:
        return response.json()
    else:
        return []

def consultar_todas_as_datas():
    return {
        "moto": consultar_datas(TIPO_EXAME_MOTO),
        "carro": consultar_datas(TIPO_EXAME_CARRO),
    }