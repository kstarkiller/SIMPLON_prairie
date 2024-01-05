SELECT AVG(round(prix/surface_habitable)) as prix2 FROM transactions_sample ts
WHERE type_batiment = 'Maison' AND date_transaction like '2022%'
