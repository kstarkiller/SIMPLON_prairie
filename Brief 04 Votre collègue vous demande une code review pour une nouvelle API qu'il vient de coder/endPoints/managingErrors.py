from typing import Union
from fastapi import HTTPException
import sqlite3

# GESTION DES ERREURS ET DES NULLS
def result_validation(result, fiscalIncome: Union[str, None] = None, room: Union[str, None] = None, year: Union[str, None] = None) :
    try:
        if result is None or len(result) == 0 or result[0] == 0 or result[0] is None :
            raise HTTPException(status_code=400, detail=f"Aucune valeur pour cette entrée")
        
        if fiscalIncome and (not fiscalIncome.isdigit() or not len(fiscalIncome) >= 5) :
            raise HTTPException(status_code=400, detail="Revenu fiscal saisie incorrect: Merci de saisir une valeur numérique de 6 chiffres")
        
        if room and not room.isdigit() :
            raise HTTPException(status_code=400, detail="Nombre de pièce saisi incorrect: Merci de saisir un entier inférieur à 10.")
        
        if year and (not year.isdigit() or not (len(year) == 4)):
            raise HTTPException(status_code=400, detail="Année saisie incorrecte: Merci de saisir une valeur numérique de 4 chiffres")
        
        return result
    
    except sqlite3.Error :
        raise HTTPException(status_code=500, detail=f"Database error")