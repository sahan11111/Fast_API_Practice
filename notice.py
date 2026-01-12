from fastapi import APIRouter

router=APIRouter(tags=["Notice"])


@router.get("/notice")
async def notice():
    return {"message": "Notice displayed"}