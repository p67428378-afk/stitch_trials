from fastapi import APIRouter

router = APIRouter(
    prefix="/tracking",
    tags=["tracking"],
    responses={404: {"description": "Not found"}},
)

@router.get("/live")
def get_live_operations():
    # Mock data for live operations
    return {
        "active_units": 2482,
        "zone_alert": "High Traffic",
        "location": "London"
    }

@router.get("/progress")
def get_ride_progress():
    # Mock data for ride progress
    return [
        {"trip_id": "TRIP-9021", "eta": "4 MIN", "status": "In-progress: Marylebone to Soho", "progress": 75},
        {"trip_id": "TRIP-8843", "eta": "12 MIN", "status": "In-progress: Heathrow to Victoria", "progress": 30},
        {"trip_id": "TRIP-9102", "eta": "DELAYED", "status": "Alert: Heavy Traffic on M4", "progress": 90, "alert": True},
    ]
