# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:31:00 2022

@author: 39333-gf
"""
import uvicorn
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import nest_asyncio
nest_asyncio.apply()
class Dati(BaseModel):
    Age: float
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float
        
app = FastAPI()

with open("model1.pkl", "rb") as f:
    model = pickle.load(f)


@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}


@app.post('/prediction')
def get_dati_category(data: Dati):
    received = data.dict()
    Age = received['Age']
    Height = received['Height']
    Weight = received['Weight']
    Duration = received['Duration']
    Heart_Rate = received['Heart_Rate']
    Body_Temp = received['Body_Temp']
    pred_name = model.predict([[Age,Height,Weight,Duration,Hearth_Rate,Body_Temp]]).tolist()[0]                              
    return {'prediction': pred_name}


@app.get('/predict')
def get_cat(Age: float,Height: float, Weight: float, Duration: float, Hearth_Rate: float, Body_Temp: float):
    pred_name = model.predict([[Age,Height,Weight,Duration,Hearth_Rate,Body_Temp]]).tolist()[0]            
    return {'prediction': pred_name}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)    