from fastapi import APIRouter

router=APIRouter()


@router.get("/notice")
async def notice():
    return {"message": "Notice displayed"}