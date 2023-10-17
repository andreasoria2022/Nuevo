import pandas as pd
from fastapi import FastAPI

userdata= pd.read_csv('../Data/userdata.csv')

app = FastAPI()

@app.get("/userdata/{user_id}")
async def userdata(user_id: str):
    usuario= userdata[userdata['user_id']== user_id]

    if len(usuario)==0:
        return 'El usuario no existe'
    
    dinero_gastado = usuario['dinero_gastado'].values[0]
    porcentaje_recomendación = usuario['porcentaje de recomendacion'].values[0]
    items_count = usuario['items_count'].values[0]

    user_data = {
            "Cantidad de dinero gastado": dinero_gastado,
            "Porcentaje de recomendación": porcentaje_recomendación,
            "cantidad de items": items_count
        }

    return user_data
    
    
    
    
    
   


    