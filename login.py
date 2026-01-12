from fastapi import APIRouter


'''tags use to seprate the login section in swagger docs'''

router=APIRouter(prefix="/hello",tags=["Login"])

@router.get("/login")
async def login():
    return {"message": "Login successful"}


@router.get("/logout")
async def logout():
    return {"message": "logout successful"}