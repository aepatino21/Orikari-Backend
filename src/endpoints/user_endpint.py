from config.supabase_config import supabase
from schemas.user import User, UserCreate, UserUpdate, UserDelete, UserGet
from fastapi import APIRouter, HTTPException
from typing import List


# Create a router instance
router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Get all users
@router.get("/", response_model=List[UserGet])
async def get_all_users():
    """
    Get all users from the database.
    """
    try:
        response = (
            supabase.table("Usuario")
            .select("*")
            .execute()
        )

        data = response.data
        users= []
        for user in data:
            user.append({
                "id": user.get("id"),
                "username": user.get("username"),
                "created_at": user.get("created_at"),
                "name": user.get("name"),
                "correo": user.get("correo"),
                "rol": user.get("rol"),
                "is_expert": user.get("is_expert")
            })
            users.append(user)

        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        # if response.data:
        #     return response.data
        # else:
        #     raise HTTPException(status_code=404, detail="No users found")
    
# Create user
@router.post("/add")
async def create_user(user: UserCreate):
    """
    Create a new user in the database.
    """
    try:
        # Check if the user already exists with the same email or username
        existing_user = (
            supabase.table("User")
            .select("*")
            .eq("correo", user.correo)
            .or_("username.eq." + user.username)
            .execute()
        )

        if existing_user.data:
            raise HTTPException(status_code=400, detail="User already exists")
        
        # Insert the new user into the database
        
        response = (
            supabase.table("User")
            .insert(user.dict())
            .execute()
        )

        if response.data:
            return response.data
        else:
            raise HTTPException(status_code=404, detail="User not created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Update user
