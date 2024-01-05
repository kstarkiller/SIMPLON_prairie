SELECT ville, count(id_transaction) as n_transaction, SUM(prix) as tot_prix FROM transactions_sample ts 
GROUP BY ville 
ORDER BY tot_prix DESC
LIMIT 10


-- En tant que CEO, je veux consulter le top 10 des villes les plus dynamiques en termes de transactions immobilières

