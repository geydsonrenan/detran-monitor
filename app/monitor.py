from app.api import consultar_todas_as_datas
from app.notifier import EmailNotifier
from app.state import load_state, save_state
from app.config import (
    EMAIL
)
from datetime import datetime
import logging
import sys

def tocar_alerta_sonoro():
    try:
        if sys.platform == "win32":
            import winsound
            # Emite 3 bips (Frequência: 1000Hz, Duração: 300ms)
            for _ in range(3):
                winsound.Beep(1000, 300)
        else:
            # Fallback para Linux/macOS no terminal
            print('\a')
    except Exception as e:
        logging.warning(f"Falha ao reproduzir o som do alerta: {e}")

class Monitor:

    def __init__(self):

        self.notifier = EmailNotifier(EMAIL)

    def verificar(self):

        state = load_state()

        resultados = consultar_todas_as_datas()

        print(resultados)

        for categoria, datas in resultados.items():

            if not state[categoria]["enabled"]:
                continue

            datas_atuais = set(datas)
            datas_anteriores = set(state[categoria]["last_dates"])

            novas_datas = datas_atuais - datas_anteriores

            if novas_datas:
                tocar_alerta_sonoro()
                self.notifier.send(
                    categoria,
                    sorted(novas_datas)
                )
                logging.info(f"---------- {categoria} ----------")
                logging.info(f"{novas_datas}")
            else:
                logging.info(f"Nenhuma atualização para {categoria} -- {datetime.now()}")

            state[categoria]["last_dates"] = sorted(datas)

        save_state(state)