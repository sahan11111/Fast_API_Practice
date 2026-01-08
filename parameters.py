
from fastapi import APIRouter
# Example endpoint with query parameter
router = APIRouter()

@router.get("/sahan")
def read_sahan(name: str):
    return {"message": f"Hello, {name}!"}