from pydantic import BaseModel, EmailStr


## pip install pydantic[email] to use EmailStr type

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int


user = User(name="daniel", email='daniel@gmail.com', account_id=90000)
print(user.email)
