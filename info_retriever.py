import requests

STARSHIPS_API = "https://swapi.py4e.com/api/starships"

def get_all_starships():
    all_responses = []
    for x in range(1,5):
        repsonse = requests.get(STARSHIPS_API+f"?page={x}").json()
        for starship in repsonse["results"]:
            all_responses.append(starship)
    return all_responses

def order_starships_by_name(all_starships, direction):
    if direction == 'asc':
        ordered_starships_by_name = sorted(all_starships, key=lambda k: k["name"].upper())
    elif direction == 'desc':
        ordered_starships_by_name = sorted(all_starships, key=lambda k: k["name"].upper(), reverse=True)
    return ordered_starships_by_name

def display_ordered_starships_by_name_asc():
    all_starships = get_all_starships()
    ordered_starships = order_starships_by_name(all_starships, 'asc')
    return ordered_starships

def display_ordered_starships_by_name_desc():
    all_starships = get_all_starships()
    ordered_starships = order_starships_by_name(all_starships, 'desc')
    return ordered_starships

def order_starships_by_cost(all_starships, direction):
    if direction == 'asc':
        ordered_starships_by_cost = sorted(all_starships, key=lambda k: int(k["cost_in_credits"]) if k["cost_in_credits"].isdigit() else float("inf"))
    elif direction == 'desc':
        ordered_starships_by_cost = sorted(all_starships, key=lambda k: int(k["cost_in_credits"]) if k["cost_in_credits"].isdigit() else float("inf"), reverse=True)
    return ordered_starships_by_cost
    
def display_ordered_starships_by_cost_asc():
    all_starships = get_all_starships()
    ordered_starships = order_starships_by_cost(all_starships, 'asc')
    return ordered_starships

def display_ordered_starships_by_cost_desc():
    all_starships = get_all_starships()
    ordered_starships = order_starships_by_cost(all_starships, 'desc')
    return ordered_starships

##Testing
if __name__ == "__main__":
    #print(get_all_starships())
    all_starships = get_all_starships()
    #ordered_starships = order_starships_by_name(all_starships)

    print(display_ordered_starships_by_cost_desc())
