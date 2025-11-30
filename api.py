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
    if filters.filter and filters.order:
        return {"filter" : filters.filter, "order": filters.order}
    return info_retriever.display_ordered_starships_by_name_asc()

# @app.get('/starships')
# def get_starships_req():
#     return info_retriever.display_ordered_starships_by_name_asc()

# @app.get('/starships/{order}')
# def get_starships_req(order):
#     if order == 'asc':
#         return info_retriever.display_ordered_starships_by_name_asc()
#     elif order == 'desc':
#         return info_retriever.display_ordered_starships_by_name_desc()
#     else:
#         raise HTTPException(status_code=400, detail="Please enter asc or desc for order")
    
# @app.get('/starships/cost/{order}')
# def get_starships_by_cost_req(order):
#     if order == 'asc':
#         return info_retriever.display_ordered_starships_by_cost_asc()
#     elif order == 'desc':
#         return info_retriever.display_ordered_starships_by_cost_desc()
#     else:
#         raise HTTPException(status_code=400, detail="Please enter asc or desc for order")