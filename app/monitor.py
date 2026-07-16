from app.api import consultar_todas_as_datas
from app.notifier import EmailNotifier
from app.state import load_state, save_state
from app.config import (
    EMAIL
)
from datetime import datetime

class Monitor:

    def __init__(self):

        self.notifier = EmailNotifier(EMAIL)

    def verificar(self):

        state = load_state()

        resultados = consultar_todas_as_datas()

        for categoria, datas in resultados.items():

            if not state[categoria]["enabled"]:
                continue

            datas_atuais = set(datas)
            datas_anteriores = set(state[categoria]["last_dates"])

            novas_datas = datas_atuais - datas_anteriores

            if novas_datas:
                self.notifier.send(
                    categoria,
                    sorted(novas_datas)
                )
                print(f"---------- {categoria} ----------")
                print(f"{novas_datas}")
            else:
                print(f"Nenhuma atualização para {categoria} -- {datetime.now()}")

            state[categoria]["last_dates"] = sorted(datas)

        save_state(state)