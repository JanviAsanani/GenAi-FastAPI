from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

class CodeFile(BaseModel):
    id: int
    content: str
    owner_id: int

class DebugRequest(BaseModel):
    code: str