from fastapi import FastAPI
import pickle
import uvicorn
import numpy as np

app = FastAPI()

# LOADS DES MODELES 
with open(r"C:\Users\Utilisateur\local_SIMPLON\SIMPLON_prairie\Brief 12012024 Développer une API REST pour exposer un modèle prédictif avec des données immobilières\model\paris_model.pkl", "rb") as f:
    my_unpickler = pickle.Unpickler(f)
    paris_model = my_unpickler.load()

with open(r"C:\Users\Utilisateur\local_SIMPLON\SIMPLON_prairie\Brief 12012024 Développer une API REST pour exposer un modèle prédictif avec des données immobilières\model\idf_model.pkl", "rb") as g:
    my_unpickler = pickle.Unpickler(g)
    idf_model = my_unpickler.load()


# DECLARATIONS DES ROUTES POST
@app.post("/sq2_price_predictor_PARIS/", description="Retourne une prédiction de prix au m²")
async def sq2_price_predictor_PARIS(longitude: str, latitude: str):
    input_data = np.array([[longitude, latitude]])

    return paris_model.predict(input_data)[0]

@app.post("/sq2_price_predictor_IDF/", description="Retourne une prédiction de prix au m²")
async def sq2_price_predictor_IDF(longitude: str, latitude: str, taux: str):
    input_data = np.array([[longitude, latitude, taux]])
    
    return idf_model.predict(input_data)[0]


uvicorn.run(app)