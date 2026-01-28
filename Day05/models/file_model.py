from database import files_col

def save_file(data: dict):
    files_col.insert_one(data)

def get_file_by_key(key: str):
    return files_col.find_one({"key": key})

def get_user_files(user_id: int):
    return files_col.find({"owner_id": user_id})
