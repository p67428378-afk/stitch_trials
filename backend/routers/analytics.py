from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"],
    responses={404: {"description": "Not found"}},
)

@router.get("/kpis")
def get_kpis():
    # Mock data for KPIs
    return {
        "total_rides": 1240,
        "active_drivers": 45,
        "avg_wait_time": "4.2 min"
    }

@router.get("/driver_performance")
def get_driver_performance():
    # Mock data for driver performance (weekly)
    return [
        {"day": "MON", "completed": 80, "rating": 4.5},
        {"day": "TUE", "completed": 65, "rating": 4.2},
        {"day": "WED", "completed": 90, "rating": 4.8},
        {"day": "THU", "completed": 75, "rating": 4.3},
        {"day": "FRI", "completed": 85, "rating": 4.6},
        {"day": "SAT", "completed": 40, "rating": 3.9},
        {"day": "SUN", "completed": 30, "rating": 3.5},
    ]
