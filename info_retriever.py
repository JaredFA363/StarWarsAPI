import requests

STARSHIPS_API = "https://swapi.py4e.com/api/starships"

def get_all_starships():
    all_responses = []
    for x in range(1,5):
        repsonse = requests.get(STARSHIPS_API+f"?page={x}").json()
        for starship in repsonse["results"]:
            all_responses.append(starship)
    return all_responses

def apply_filters_to_starships(filter_name, filter_order):
    all_starships = get_all_starships()
    if filter_name == None and filter_order == None:
        return all_starships
    elif filter_name == "name" and filter_order == "asc":
        ordered_starships = sorted(all_starships, key=lambda k: k["name"].upper())
        return ordered_starships
    elif filter_name == "name" and filter_order == "desc":
        ordered_starships = sorted(all_starships, key=lambda k: k["name"].upper(), reverse=True)
        return ordered_starships
    elif filter_name == "cost" and filter_order == "asc":
        ordered_starships = sorted(all_starships, key=lambda k: int(k["cost_in_credits"]) if k["cost_in_credits"].isdigit() else float("inf"))
        return ordered_starships
    elif filter_name == "cost" and filter_order == "desc":
        ordered_starships = sorted(all_starships, key=lambda k: int(k["cost_in_credits"]) if k["cost_in_credits"].isdigit() else float("inf"), reverse=True)
        return ordered_starships
    elif filter_name == "length" and filter_order == "asc":
        ordered_starships = sorted(all_starships, key=lambda k: float(k["length"]) if k["length"].isdigit() else float("inf"))
        return ordered_starships
    elif filter_name == "length" and filter_order == "desc":
        ordered_starships = sorted(all_starships, key=lambda k: float(k["length"]) if k["length"].isdigit() else float("inf"), reverse=True)
        return ordered_starships
    else:
        return "incorrect filters"
