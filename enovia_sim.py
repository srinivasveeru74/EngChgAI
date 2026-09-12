import json, pathlib

DATA = pathlib.Path(“data/sample_cos.json”)

class EnoviaSim:
    “““Mirrors the ENOVIA REST shape; replays sample data.”””

    def get_change_order(self, co_id: str) -> dict:
        for co in json.loads(DATA.read_text()):
            if co[“id”] == co_id:
                return co
        raise KeyError(co_id)

    def list_open_cos(self) -> list:
        return json.loads(DATA.read_text())
