from fastapi import APIRouter

router=APIRouter()


@router.get("/news")
async def news():
    #all codes here
    return {"message": "News fetched"}