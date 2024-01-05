SELECT prix, surface_habitable, AVG(ROUND(prix/surface_habitable)) as prix2  FROM transactions_sample ts
WHERE ville = 'AVIGNON' AND date_transaction like '2022%' AND type_batiment = 'Maison'
