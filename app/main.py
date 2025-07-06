import zoneinfo
from datetime import datetime
import time

from fastapi import FastAPI, Request
from sqlmodel import select

from db import SessionDep, create_all_tables
from models import Invoice, Transaction

from .routers import customers, plans, transactions

app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(plans.router)


@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url} completed in: {process_time:.4f} seconds")

    return response


@app.get("/")
async def root():
    return {"message": "hola mundo"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
    "MAD": "Europe/Madrid",
}

formats = {
    "CO": "%Y-%m-%d %H:%M:%S",
    "MX": "%Y-%m-%d %H:%M:%S",
    "AR": "%Y-%m-%d %H:%M:%S",
    "BR": "%Y-%m-%d %H:%M:%S",
    "PE": "%Y-%m-%d %H:%M:%S",
    "MAD": "%Y-%m-%d %H:%M:%S"
}

@app.get("/tiempo/{iso_code}")
async def get_time_by_eso_code(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if not timezone_str:
        return {"error": "Código de país no soportado"}
    tz = zoneinfo.ZoneInfo(timezone_str)
    city_name = timezone_str.split("/")[-1].replace("_", " ")
    now = datetime.now(tz)
    # Ejemplo: 2025-06-23 20:15:00 Madrid CEST
    time_str = f"{now.strftime(formats.get(iso))} {city_name} {now.strftime('%Z')}"
    return {"time": time_str}


@app.post("/invoices", response_model=Invoice)
async def create_invoice(invoice_data: Invoice):
    breakpoint()
    return invoice_data
