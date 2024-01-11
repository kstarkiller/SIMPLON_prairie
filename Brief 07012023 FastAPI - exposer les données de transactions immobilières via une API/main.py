from fastapi import FastAPI
import uvicorn
from endPoints.managingErrors import result_validation
import endPoints.fonctions as f

app = FastAPI(title="Real Estate Transactions API")

app.get("/avg_fiscal_income/")(f.avg_fiscal_income)
app.get("/top10_transactions/")(f.top10_transactions)
app.get("/transactions_count/")(f.transactions_count)
app.get("/avg_sq2_price/")(f.avg_sq2_price)
app.get("/n_rooms_count/")(f.n_rooms_count)
app.get("/n_rooms_distrib/")(f.n_rooms_distrib)
app.get("/avg_sq2_price_by_building/")(f.avg_sq2_price_by_building)
app.get("/transactions_count_by_district/")(f.transactions_count_by_district)
app.get("/transactions_count_under_income/")(f.transactions_count_under_income)
app.get("/top10_dynamic_cities/")(f.top10_dynamic_cities)
app.get("/cheapest_flats_sq2_price_top10_cities/")(f.cheapest_flats_sq2_price_top10_cities)
app.get("/highest_houses_sq2_price_top10_cities/")(f.highest_houses_sq2_price_top10_cities)

uvicorn.run(app)