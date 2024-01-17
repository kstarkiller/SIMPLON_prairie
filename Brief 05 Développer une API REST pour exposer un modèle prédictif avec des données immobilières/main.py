from fastapi import FastAPI, HTTPException
import pickle
import uvicorn
import numpy as np

app = FastAPI()

with open(r"C:\Users\Utilisateur\local_SIMPLON\SIMPLON_prairie\Brief 12012024 Développer une API REST pour exposer un modèle prédictif avec des données immobilières\model\coordinatesOnly_model.pkl", "rb") as f:
    my_unpickler = pickle.Unpickler(f)
    coordinatesOnly_model = my_unpickler.load()

with open(r"C:\Users\Utilisateur\local_SIMPLON\SIMPLON_prairie\Brief 12012024 Développer une API REST pour exposer un modèle prédictif avec des données immobilières\model\withInterestRates_model.pkl", "rb") as g:
    my_unpickler = pickle.Unpickler(g)
    withInterestRates_model = my_unpickler.load()

@app.post("/sq2_price_predictor_v1/", description="Retourne une prédiction de prix au m²")
async def sq2_price_predictor(longitude: float, latitude: float):
    input_data = np.array([[longitude, latitude]])

    return coordinatesOnly_model.predict(input_data)[0]

@app.post("/sq2_price_predictor_v2/", description="Retourne une prédiction de prix au m²")
async def sq2_price_predictor(longitude: float, latitude: float, taux: float):
    input_data = np.array([[longitude, latitude, taux]])

    return withInterestRates_model.predict(input_data)[0]


uvicorn.run(app)