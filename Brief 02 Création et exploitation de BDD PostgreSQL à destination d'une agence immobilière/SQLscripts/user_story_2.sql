SELECT ville, id_transaction, date_transaction, prix FROM transactions_sample ts
WHERE ville in ('HENDAYE','POITIERS','TOULOUSE') OR ville like 'PARIS%'
ORDER BY date_transaction DESC
LIMIT 10
