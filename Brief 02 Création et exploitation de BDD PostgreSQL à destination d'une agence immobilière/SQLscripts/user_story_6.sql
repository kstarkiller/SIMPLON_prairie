SELECT n_pieces, count(id_transaction) as n_bien  FROM transactions_sample ts
-- WHERE ville like 'MARSEILLE%' AND date_transaction like '2022%' AND type_batiment = 'Appartement'
GROUP BY n_pieces
