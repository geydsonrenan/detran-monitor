import json
from pathlib import Path

STATE_FILE = Path("data/state.json")


DEFAULT_STATE = {
    "moto": {
        "enabled": True,
        "last_available": False
    },
    "carro": {
        "enabled": True,
        "last_available": False
    }
}


def load_state():
    if not STATE_FILE.exists():
        save_state(DEFAULT_STATE)
        return DEFAULT_STATE

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    STATE_FILE.parent.mkdir(exist_ok=True)

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)