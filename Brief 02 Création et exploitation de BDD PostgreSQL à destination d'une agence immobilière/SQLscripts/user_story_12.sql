SELECT ville, type_batiment, AVG(ROUND(prix/surface_habitable)) as prix2moyen FROM transactions_sample ts 
WHERE type_batiment = 'Maison'
GROUP BY ville 
ORDER BY prix2moyen DESC
LIMIT 10


-- En tant que CEO, je veux accéder aux 10 villes avec un prix au m2 moyen le plus haut pour les maisons


