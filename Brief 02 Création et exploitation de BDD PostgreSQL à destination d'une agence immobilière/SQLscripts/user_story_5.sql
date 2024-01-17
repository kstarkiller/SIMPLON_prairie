SELECT count(id_transaction) FROM transactions_sample ts
WHERE n_pieces = 1 AND date_transaction like '2022%'
