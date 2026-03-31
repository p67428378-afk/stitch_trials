from fastapi import FastAPI
from backend.app.database import Base, engine
from backend.app.routers import users, cabs, bookings, payments, tracking, reports

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(cabs.router)
app.include_router(bookings.router)
app.include_router(payments.router)
app.include_router(tracking.router)
app.include_router(reports.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cab Management System API"}
