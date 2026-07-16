import resend

from app.config import (
    RESEND_API_KEY,
    EMAIL_FROM,
)


class EmailNotifier:

    def __init__(self, dest: str):
        self.dest = dest
        resend.api_key = RESEND_API_KEY

    def send(self, categoria: str, dates: list[str]):

        html = f"""
        <h2>🚨 Vagas encontradas!</h2>

        <p><strong>Categoria:</strong> {categoria}</p>

        <p>Datas disponíveis:</p>

        <ul>
            {''.join(f'<li>{data}</li>' for data in dates)}
        </ul>
        """

        resend.Emails.send({
            "from": EMAIL_FROM,
            "to": self.dest,
            "subject": "🚨 Vagas no DETRAN",
            "html": html,
        })