from fastapi import FastAPI, HTTPException
import pickle
import uvicorn
import numpy as np

app = FastAPI()

with open(r"C:\Users\Utilisateur\local_SIMPLON\SIMPLON_prairie\Brief 12012024 Développer une API REST pour exposer un modèle prédictif avec des données immobilières\model\model_RandomForestRegressor.pkl", "rb") as f:
    my_unpickler = pickle.Unpickler(f)
    model = my_unpickler.load()

@app.get("/sq2_price_predictor/", description="Retourne une prédiction de prix au m²")
async def sq2_price_predictor(latitude: float, longitude: float):
    input_data = np.array([[latitude, longitude]])

    return model.predict(input_data)[0]


uvicorn.run(app)