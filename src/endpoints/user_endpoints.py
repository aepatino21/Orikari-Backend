from config.supabase_config import supabase
from schemas.user import User, UpdateUser, DeleteUser, InsertUser
from fastapi import APIRouter, HTTPException
from typing import List


# Create a router instance
router = APIRouter(
    prefix="/user",
    tags=["User"]
)

users_router = router

# Get all users
@router.get("/", response_model=List[User])
async def get_all_users() -> List[User]:
    try:
        response = (
            supabase.table("User")
            .select("*")
            .execute()
        )

        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get User by ID.
@router.get('/{id}')
async def getuser_byid(id: int) -> User:
    try:
        response = (
            supabase.table("User")
            .select("*")
            .eq("id", id)
            .execute()
        )

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))


# Create user
@router.post("/add", response_model = User)
async def create_user(user: InsertUser) -> User:
    try:
        user_data = user.model_dump(exclude_none = True)
        user_data["role"] = user.role.lower()

        # Check if the user already exists with the same email or username
        existing_user = (
            supabase.table("User")
            .select("*")
            .or_("username.eq." + user_data["username"] + ",mail.eq." + user_data["mail"])  
            .execute()
        )

        if existing_user.data:
            raise HTTPException(status_code = 400, detail = "User already exists")
        
        # Insert the new user into the database
        
        response = (
            supabase.table("User")
            .insert(user_data)
            .execute()
        )

        if response.data:
            return response.data[0]
        else:
            raise HTTPException(status_code = 404, detail = "User not created")
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))
    
# Update user
@router.put("/update", response_model = User)
async def update_user(user: UpdateUser) -> User:
    try:
        user_data = user.model_dump(exclude_none = True)

        response = (
            supabase.table("User")
            .update(user_data)
            .eq("id", user_data["id"])
            .execute()
        )

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

# Delete User
@router.delete("/delete", response_model = User)
async def delete_user(user: DeleteUser) -> User:
    try:
        user_data = user.model_dump()

        response = (
            supabase.table("User")
            .delete()
            .eq("id", user_data["id"])
            .execute()
        )

        return response.data
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

    
