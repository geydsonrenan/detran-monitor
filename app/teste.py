from app.config import EMAIL
from app.notifier import EmailNotifier


if __name__ == "__main__":
    notifier = EmailNotifier(EMAIL)
    notifier.send(
        "Moto",
        [
            "10/08/2026",
            "11/08/2026",
        ],
    )