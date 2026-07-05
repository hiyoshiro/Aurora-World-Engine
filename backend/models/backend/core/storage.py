import json
import uuid
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

FILES = {
    "projects": DATA_DIR / "projects.json",
    "characters": DATA_DIR / "characters.json",
    "personas": DATA_DIR / "personas.json",
    "sessions": DATA_DIR / "sessions.json",
}


def now():
    return datetime.now().isoformat(timespec="seconds")


def new_id():
    return str(uuid.uuid4())[:8]


def load_list(name: str):
    path = FILES[name]
    if not path.exists():
        save_list(name, [])
    return json.loads(path.read_text(encoding="utf-8"))


def save_list(name: str, data):
    FILES[name].write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def create_item(name: str, item: dict):
    data = load_list(name)
    item["id"] = new_id()
    item["created_at"] = now()
    item["updated_at"] = now()
    item["deleted"] = False
    data.append(item)
    save_list(name, data)
    return item


def update_item(name: str, item_id: str, updates: dict):
    data = load_list(name)
    for item in data:
        if item["id"] == item_id:
            item.update(updates)
            item["updated_at"] = now()
            save_list(name, data)
            return item
    return None


def soft_delete_item(name: str, item_id: str):
    return update_item(name, item_id, {"deleted": True})


def get_item(name: str, item_id: str):
    for item in load_list(name):
        if item["id"] == item_id and not item.get("deleted", False):
            return item
    return None


def list_items(name: str):
    return [x for x in load_list(name) if not x.get("deleted", False)]
