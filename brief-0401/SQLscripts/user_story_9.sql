SELECT ts.ville, count(ts.id_transaction) AS count FROM transactions_sample ts
LEFT JOIN foyers_fiscaux ff ON ts.ville = UPPER(ff.ville) 
WHERE ts.date_transaction like '2022%' AND ff.revenu_fiscal_moyen > 40000 AND ff.date = 2018
GROUP BY ts.ville

-- En tant que CEO je souhaite connaitre le nombre total de vente d'appartements en 2022
-- dans toutes les villes où le revenu fiscal moyen en 2018 est supérieur à 40k
