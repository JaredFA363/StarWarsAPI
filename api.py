'''
Your service should present an API which:

Surfaces a list of starships sorted by name - GET - param: no

Allow the sort order to be ascending or descending - GET - param: Ascending or Descending

Allow the sort key to be changed (e.g. sort by length or cost rather than name) - allow what field they want to sort by 
'''

from fastapi import FastAPI, HTTPException, Depends
import info_retriever
from model import FilterRequest

## API for Star Wars

app = FastAPI()

@app.get('/starships')
def get_starships_request(filters: FilterRequest = Depends()):
    possible_filters = ["cost", "name", "length"]
    possible_orders = ["asc", "desc"]
    #return {filters.filter: filters.order}

    if filters.filter and filters.order:
        if filters.filter not in possible_filters:
            raise HTTPException(status_code=400, detail="Filters must be on of cost,name or length")
        elif filters.order not in possible_orders:
            raise HTTPException(status_code=400, detail="Order must be asc or desc")
        else:
            return info_retriever.apply_filters_to_starships(filters.filter, filters.order)
    return info_retriever.apply_filters_to_starships(None,None)