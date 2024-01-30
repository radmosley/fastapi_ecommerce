from pydantic import BaseModel

class AccountIn(BaseModel):
    username: str
    email: str
    password: str

class AccountOut(BaseModel):
    account_id: int
    username: str
    email: str