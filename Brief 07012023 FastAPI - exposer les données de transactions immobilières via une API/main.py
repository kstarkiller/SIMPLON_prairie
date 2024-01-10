from typing import Union
from fastapi import FastAPI, HTTPException
import sqlite3
import uvicorn

app = FastAPI()

# Connexion vers la db à utiliser pour faciliter la correction du brief
con = sqlite3.connect("Chinook.db")

# Connexion vers la db à utiliser pour exploiter l'API deuis ma machine
# con = sqlite3.connect(r"C:\Users\Utilisateur\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")

# GESTION DES ERREURS ET DES NULLS
# Permet de vérifier le format de l'année
def validate_year(year: str):
    if not year.isdigit() or not (len(year) == 4) :
        raise HTTPException(status_code=400, detail="Année saisie incorrecte: Merci de saisir une valeur numérique de 4 chiffres")
    return year

# Permet de vérifier le format du nombre de pièce
def validate_room(room: str):
    if not room.isdigit() :
        raise HTTPException(status_code=400, detail="Nombre de pièce saisi incorrect: Merci de saisir un entier inférieur à 10.")
    return room

# Permet de vérifier le format du revenu fiscal
def validate_fiscalIncome(fiscalIncome: str):
    if not fiscalIncome.isdigit() or not len(fiscalIncome) >= 5 :
        raise HTTPException(status_code=400, detail="Revenu fiscal saisie incorrect: Merci de saisir une valeur numérique de 6 chiffres")
    return fiscalIncome

# Permet de renvoyer une erreur lorsque la réponse de la requète est vide
def result_validation(result) :
    if result is None or len(result) == 0 or result[0] == 0 or result[0] is None:
        raise HTTPException(status_code=400, detail=f"Aucune valeur pour cette entrée")
    return result

# REQUETE 1
# Fonction requêtant le revenu fiscal moyen en 2021
@app.get("/avg_fiscal_income/", description="Retourne le revenu fiscal moyen total d'une ville donnée")
async def avg_fiscal_income(city: str):
    cur = con.cursor()
    req = f"""SELECT revenu_fiscal_moyen, date, ville FROM foyers_fiscaux
    WHERE ville like \'{city}%\' AND date = 2021;"""
    
    result = cur.execute(req).fetchall()

    return result_validation(result)

# REQUETE 2
# Fonction requêtant le top 10 des transactions ordonné par date descendante
# avec la possibilité de filtrer par ville
@app.get("/top10_transactions/", description="Retourne les 10 dernières transactions de la base entière ou d'une ville donnée")
async def top10_transactions(city: Union[str, None] = None):
    cur = con.cursor()
    if city :
        req = f'''SELECT ville, id_transaction, date_transaction, prix FROM transactions_sample
        WHERE ville like \'{city}%\'
        ORDER BY date_transaction DESC LIMIT 10;'''
    else :
        req = '''SELECT ville, id_transaction, date_transaction, prix FROM transactions_sample
        ORDER BY date_transaction DESC LIMIT 10;'''
    
    result = cur.execute(req).fetchall()

    return result_validation(result)

# REQUETE 3
# Fonction requêtant le nombre total de transaction
# avec la possibilité de filtrer par ville et par année
@app.get("/transactions_count/", description="Retourne le nombre de transactions de la base entière ou d'une ville et/ou année donnée")
async def transactions_count(city: Union[str, None] = None, year: Union[str, None] = None):
    cur = con.cursor()
    if city and not year :
        req = f'''SELECT COUNT(id_transaction) FROM transactions_sample ts
        WHERE ville like \'{city}%\''''
    elif year and not city :
        year = validate_year(year)
        req = f'''SELECT COUNT(id_transaction) FROM transactions_sample ts
        WHERE date_transaction like \'{year}%\''''
    elif city and year :
        year = validate_year(year)
        req = f'''SELECT COUNT(id_transaction) FROM transactions_sample ts
        WHERE ville like \'{city}%\' AND date_transaction like \'{year}%\''''
    else :
        req = 'SELECT COUNT(id_transaction) FROM transactions_sample;'
    
    result = cur.execute(req).fetchone()

    return result_validation(result)

# REQUETE 4
# Fonction requêtant la moyenne du prix au m²
# avec la possibilité de filtrer par année
@app.get("/avg_sq2_price/", description="Retourne le prix au m² moyen pour un type de bâtiment donné")
async def avg_sq2_price(buildingType: str, year: Union[str, None] = None):
    cur = con.cursor()
    if year :
        year = validate_year(year)
        req = f"""SELECT AVG(round(prix/surface_habitable)) as prix2 FROM transactions_sample
        WHERE type_batiment = \"{buildingType}\" AND date_transaction like \'{year}%\'"""
    else :
        req = f"""SELECT AVG(round(prix/surface_habitable)) as prix2 FROM transactions_sample
        WHERE type_batiment = \"{buildingType}\""""
    
    result = cur.execute(req).fetchone()

    return result_validation(result)

# REQUETE 5
# Fonction requêtant le nombre de bien avec un nombre de pièce donné
# avec la possibilité de filtrer par année
@app.get("/nb_rooms_count/", description="Retourne le nombre de bien avec un nombre de pièce donné")
async def n_rooms_count(nb_room: str, year: Union[str, None] = None):
    cur = con.cursor()
    nb_room = validate_room(nb_room)
    if not year :
        req = f"""SELECT count(id_transaction) FROM transactions_sample
        WHERE n_pieces = {nb_room}"""
    else :
        year = validate_year(year)
        req = f"""SELECT count(id_transaction) FROM transactions_sample
        WHERE n_pieces = {nb_room} AND date_transaction like '{year}%'"""   

    result = cur.execute(req).fetchone()

    return result_validation(result)

# REQUETE 6
# Fonction requêtant la répartition du nombre de bien par nombre de pièce
# avec la possibilité de filtrer par année
@app.get("/nb_rooms_distrib/", description="Retourne la répartition du nombre de bien par nombre de pièce")
async def n_rooms_distrib(year: Union[str, None] = None):
    cur = con.cursor()
    if year :
        year = validate_year(year)
        req = f"""SELECT n_pieces, count(id_transaction)  FROM transactions_sample
        WHERE date_transaction like '{year}%'
        GROUP BY n_pieces"""
    else:
        req = f"""SELECT n_pieces, count(id_transaction)  FROM transactions_sample
        GROUP BY n_pieces""" 

    result = cur.execute(req).fetchall()

    return result_validation(result)

# REQUETE 7
# Fonction requêtant la moyenne du prix au m² par type de batiment
# avec la possibilité de filtrer par année
@app.get("/avg_sq2_price_by_building/", description="Retourne la moyenne du prix au m² par type de batiment")
async def avg_sq2_price_by_building(buildingType: Union[str, None] = None, year: Union[str, None] = None):
    cur = con.cursor()
    if buildingType and not year :
        result = cur.execute(f'''SELECT AVG(ROUND(prix/surface_habitable)) FROM transactions_sample
        WHERE type_batiment = \'{buildingType}\' GROUP BY type_batiment''').fetchone()
    elif not buildingType and year :
        year = validate_year(year)
        result = cur.execute(f'''SELECT AVG(ROUND(prix/surface_habitable)), type_batiment FROM transactions_sample
        WHERE date_transaction like '{year}%' GROUP BY type_batiment''').fetchall()
    elif buildingType and year :
        year = validate_year(year)
        result = cur.execute(f'''SELECT AVG(ROUND(prix/surface_habitable)) FROM transactions_sample
        WHERE type_batiment = \'{buildingType}\' AND date_transaction like '{year}%'
        GROUP BY type_batiment''').fetchone()
    else :
        result = cur.execute(f'''SELECT AVG(ROUND(prix/surface_habitable)), type_batiment FROM transactions_sample
        GROUP BY type_batiment''').fetchall()

    return result_validation(result)

# REQUETE 8
# Fonction requêtant le nombre de transaction par département
# avec la possibilité de filtrer par année
@app.get("/transactions_count_by_district/", description="Retourne le nombre de transaction par département")
async def transactions_count_by_district(year: Union[str, None] = None):
    cur = con.cursor()
    if year :
        year = validate_year(year)
        req = f'''SELECT departement, count(id_transaction) FROM transactions_sample
        WHERE date_transaction like '{year}%'
        GROUP BY departement ORDER BY departement ASC'''
    else :
        req = f'''SELECT departement, count(id_transaction) FROM transactions_sample
        GROUP BY departement ORDER BY departement ASC'''

    result = cur.execute(req).fetchall()

    return result_validation(result)

# REQUETE 9
# Fonction requêtant le nombre de transaction sur une année donnée dans toutes les villes
# ou le revenu fiscal de l'année n-4 est supérieur à un revenu fiscal donné
# avec la possibilité de filtrer par année
@app.get("/transactions_count_under_income/", description="""Retourne le nombre de transaction d'une année par ville où le revenu
         fiscal de l'année n-4 est supérieur à un revenu fiscal donné""")
async def transactions_count_under_income(fiscalIncome2YearsAgo: str, year: str):
    cur = con.cursor()
    year = validate_year(year)
    incomeYear = str(int(year)-4)
    fiscalIncome2YearsAgo = validate_fiscalIncome(fiscalIncome2YearsAgo)

    req = f'''SELECT ts.ville, count(ts.id_transaction) FROM transactions_sample ts
    LEFT JOIN foyers_fiscaux ff ON ts.ville = UPPER(ff.ville)
    WHERE ts.date_transaction like '{year}%'
    AND ff.revenu_fiscal_moyen >= {fiscalIncome2YearsAgo} AND ff.date = {incomeYear}
    GROUP BY ts.ville'''

    result = cur.execute(req).fetchall()

    return result_validation(result)

# REQUETE 10
# Fonction requêtant le top 10 des villes les plus dynamiques (montant total des transactions)
# avec la possibilité de filtrer par année
@app.get("/top10_dynamic_cities/", description="Retourne le top 10 des villes les plus dynamiques")
async def top10_dynamic_cities(year: Union[str, None] = None):
    cur = con.cursor()
    if year :
        year = validate_year(year)
        req = f'''SELECT ville, count(id_transaction) as n_transaction, SUM(prix) as tot_prix
        FROM transactions_sample ts WHERE date_transaction like '{year}%'
        GROUP BY ville ORDER BY tot_prix DESC LIMIT 10'''
    else :
        req = f'''SELECT ville, count(id_transaction) as n_transaction, SUM(prix) as tot_prix
        FROM transactions_sample ts GROUP BY ville
        ORDER BY tot_prix DESC LIMIT 10'''

    result = cur.execute(req).fetchall()

    return result_validation(result)

# REQUETE 11
# Fonction requêtant le top 10 des villes avec le prix au m² le plus bas pour les appartements
@app.get("/cheapest_flats_sq2_price_top10_cities/", description="Retourne le top 10 des villes avec le prix au m² le plus bas pour les appartements")
async def cheapest_flats_sq2_price_top10_cities():
    cur = con.cursor()
    req = f'''SELECT ville, AVG(ROUND(prix/surface_habitable)) as prix2moyen FROM transactions_sample ts 
    WHERE type_batiment = 'Appartement' GROUP BY ville ORDER BY prix2moyen ASC LIMIT 10'''

    result = cur.execute(req).fetchall()

    return result_validation(result)


# REQUETE 12
# Fonction requêtant le top 10 des villes avec le prix au m² le plus haut pour les maisons
@app.get("/highest_houses_sq2_price_top10_cities/", description="Retourne le top 10 des villes avec le prix au m² le plus haut pour les maisons")
async def highest_houses_sq2_price_top10_cities():
    cur = con.cursor()
    req = f'''SELECT ville, AVG(ROUND(prix/surface_habitable)) as prix2moyen FROM transactions_sample ts
    WHERE type_batiment = 'Maison' GROUP BY ville ORDER BY prix2moyen DESC LIMIT 10'''

    result = cur.execute(req).fetchall()

    return result_validation(result)

uvicorn.run(app)