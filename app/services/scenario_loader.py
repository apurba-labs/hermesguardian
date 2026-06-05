import json


def load_scenario(name: str):

    with open(
        f"app/scenarios/{name}.json",
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)