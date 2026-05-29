import requests

def test_get_pokemon_list_returns_expected_data():
    response = requests.get("https://pokeapi.co/api/v2/pokemon", headers={"User-Agent": "Googlebot"}, timeout=10)

    assert response.status_code == 200
    assert response.text is not None
    assert response.text.startswith('{"count":')

    payload = response.json()
    assert payload["count"] == 1350
    assert payload["previous"] is None
    assert payload["next"] == "https://pokeapi.co/api/v2/pokemon?offset=20&limit=20"
    assert len(payload["results"]) == 20

    first_pokemon = payload["results"][0]
    assert first_pokemon == {
        "name": "bulbasaur",
        "url": "https://pokeapi.co/api/v2/pokemon/1/",
    }

    names = {item["name"] for item in payload["results"]}
    assert {"bulbasaur", "ivysaur"}.issubset(names)
