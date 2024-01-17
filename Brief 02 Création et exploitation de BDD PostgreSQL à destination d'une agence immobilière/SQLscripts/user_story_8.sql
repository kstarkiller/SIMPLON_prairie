SELECT departement, ville, count(id_transaction) as n_bien FROM transactions_sample ts
GROUP BY departement
ORDER BY departement ASC

-- En tant que CEO, je veux consulter le nombre de transactions (tout type confondu) par département, ordonnées par ordre décroissant
