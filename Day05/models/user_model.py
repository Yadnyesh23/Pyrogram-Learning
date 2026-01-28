from database import user_cols

def get_user(user_id: int):
    return user_cols.find_one({"user_id": user_id})

def create_user(user_id: int, role="user"):
    user_cols.insert_one({
        "user_id": user_id,
        "role": role
    })

def update_role(user_id: int, role: str):
    user_cols.update_one(
        {"user_id": user_id},
        {"$set": {"role": role}}
    )
