from fastapi import FastAPI
from .database import engine, Base
from . import models # Import models to ensure they are registered with Base.metadata
from .routers import users, cabs, payments, reports, tracking

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(cabs.router)
app.include_router(payments.router)
app.include_router(reports.router)
app.include_router(tracking.router)
