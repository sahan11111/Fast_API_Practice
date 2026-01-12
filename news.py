from fastapi import APIRouter

router=APIRouter(tags=["News"])


@router.get("/news")
async def news():
    #all codes here
    
    return {"message": "News fetched"}