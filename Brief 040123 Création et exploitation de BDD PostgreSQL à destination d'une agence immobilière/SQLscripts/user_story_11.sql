SELECT ville, AVG(ROUND(prix/surface_habitable)) as prix2moyen FROM transactions_sample ts 
WHERE type_batiment = 'Appartement'
GROUP BY ville 
ORDER BY prix2moyen ASC
LIMIT 10


-- En tant que CEO, je veux accéder aux 10 villes avec un prix au m2 moyen le plus bas pour les appartements

