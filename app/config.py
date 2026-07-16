from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _get_env(name: str, default=None):
    value = os.getenv(name)
    if value is None:
        return default
    return value


CPF = _get_env("CPF")
DATA_NASCIMENTO = _get_env("DATA_NASCIMENTO")

TIPO_EXAME_MOTO = int(_get_env("TIPO_EXAME_MOTO", 1))
TIPO_EXAME_CARRO = int(_get_env("TIPO_EXAME_CARRO", 2))
COD_APTIDAO = int(_get_env("COD_APTIDAO", 4))

URL = _get_env(
    "URL",
    "https://online7.detran.pe.gov.br/MvcHabilitacao/Agendamento/PesquisarDataDisponibilidadeTecnica?",
)

HEADERS = {
    "Host": _get_env("HEADERS_HOST", "online7.detran.pe.gov.br"),
    "Referer": _get_env(
        "HEADERS_REFERER",
        "https://online7.detran.pe.gov.br/MvcHabilitacao/Agendamento/Pratico",
    ),
    "User-Agent": _get_env(
        "HEADERS_USER_AGENT",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    ),
    "X-Requested-With": _get_env("HEADERS_X_REQUESTED_WITH", "XMLHttpRequest"),
    "sec-ch-ua": _get_env(
        "HEADERS_SEC_CH_UA",
        '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    ),
}

COOKIES = {}

EMAIL = _get_env("EMAIL")

RESEND_API_KEY = _get_env("RESEND_API_KEY")
EMAIL_FROM = _get_env("EMAIL_FROM", "onboarding@resend.dev")
