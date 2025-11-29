from fastapi import FastAPI, HTTPException
import info_retriever

## API for Star Wars

app = FastAPI()

@app.get('/starships')
def get_starships_req():
    return info_retriever.display_ordered_starships_by_name_asc()