from fastapi import FastAPI
from .routers import users, bookings, tracking, payments, analytics

app = FastAPI(
    title="Cab Management System API",
    description="API for managing cab operations, bookings, tracking, payments, and analytics.",
    version="1.0.0",
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Cab Management System"}

app.include_router(users.router)
app.include_router(bookings.router)
app.include_router(tracking.router)
app.include_router(payments.router)
app.include_router(analytics.router)
