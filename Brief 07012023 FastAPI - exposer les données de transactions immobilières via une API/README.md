# FastAPI - Exposer les données de transactions immobilières via une API
## Rendu du brief  

### Contexte
En tant que dev IA, je serai régulèrement amené à créer une ou plusieurs API Rest dans le cadre de mes projets. C'est le but de ce brief.  
Pour cela, j'ai réutilisé la base SQLite contenant la data immo du [brief 04012023 Création et exploitation de BDD PostgreSQL à destination d'une agence immobilière](https://github.com/kstarkiller/SIMPLON_prairie/tree/main/Brief%20040123%20Création%20et%20exploitation%20de%20BDD%20PostgreSQL%20à%20destination%20d'une%20agence%20immobilière).  
  
J'ai utilisé :
- **FastAPI** et sa [documentation](https://fastapi.tiangolo.com/tutorial/) pour la création de mon API.
- Le serveur pour Python **Uvicorn**
- **Sqlite3** pour me connecter à la base de donnée et executer les requêtes SQL.
- Et **Swagger** pour tester votre API.

### Prérequis
Installation de FastAPI, Uvicorn et sqlite3 sur mon environnment Conda local.

### Remarques
Si vous téléchargez le dépot, vous y trouverez la base donnée afin de faciliter la revue de mon code (première connexion).  
Depuis ma machine, jutilise la deuxième connexion, c'est pourquoi je l'ai laissé dans mon code :
```py
# Connexion vers la db à utiliser pour faciliter la correction du brief
con = sqlite3.connect("Chinook.db")

# Connexion vers la db à utiliser pour exploiter l'API depuis ma machine
#con = sqlite3.connect(r"C:\Users\Utilisateur\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")
```
