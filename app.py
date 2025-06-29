from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
import motor.motor_asyncio
from datetime import datetime

# MongoDB Configuration
MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.users_db
users_collection = db.get_collection("users")

# Pydantic Model for User
class User(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    age: Optional[int] = None

# FastAPI Application
app = FastAPI()

# Utility to convert MongoDB document to Python dictionary
def user_helper(user: dict) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user.get("age"),
    }

# Function to structure response with headers
def structured_response(content, status_code=200):
    headers = {
        "Content-Security-Policy": "default-src 'self'",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Access-Control-Allow-Origin": "*",
        "Referrer-Policy": "no-referrer",
        "Permissions-Policy": "geolocation=(), microphone=()",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Expires": "0",
        "ETag": "abc123",
        "Last-Modified": "Wed, 21 Dec 2023 10:45:00 GMT",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Disposition": "inline",
        "Accept-Ranges": "bytes",
        "RateLimit-Limit": "100",
        "RateLimit-Remaining": "50",
        "RateLimit-Reset": "3600",
        "Server": "secure-api-server",
        "Date": datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT"),
        "Connection": "keep-alive",
        "Vary": "Accept-Encoding",
    }
    return JSONResponse(content=content, headers=headers, status_code=status_code)

@app.get("/users")
async def get_users():
    users = []
    async for user in users_collection.find():
        users.append(user_helper(user))
    return structured_response(users)

@app.post("/users")
async def create_user(user: User):
    user = user.dict()
    result = await users_collection.insert_one(user)
    new_user = await users_collection.find_one({"_id": result.inserted_id})
    return structured_response(user_helper(new_user))

@app.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    user = user.dict()
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    result = await users_collection.replace_one({"_id": ObjectId(user_id)}, user)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await users_collection.find_one({"_id": ObjectId(user_id)})
    return structured_response(user_helper(updated_user))

@app.patch("/users/{user_id}")
async def patch_user(user_id: str, user: dict):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    result = await users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await users_collection.find_one({"_id": ObjectId(user_id)})
    return structured_response(user_helper(updated_user))

@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    result = await users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return structured_response({"message": "User deleted successfully"})

@app.head("/users/{user_id}")
async def head_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(headers={"User-Exists": "true"})

@app.options("/users")
async def options_users():
    return JSONResponse(headers={
        "Allow": "GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD"
    })

@app.options("/users/{user_id}")
async def options_user():
    return JSONResponse(headers={
        "Allow": "GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD"
    })

# @app.connect("/connect")
# async def connect():
#     return structured_response({"message": "Tunnel established"})

@app.trace("/trace")
async def trace(request: Request):
    body = await request.body()
    return structured_response({"message": "Trace received", "echo": body.decode("utf-8")})


