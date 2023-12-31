from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

# To get coustomized responce, we can use this class:
    'Like this: only gives body in respose and excludes id & title'
class ShowBlog(BaseModel):
    body: str
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class DUser(BaseModel):
    name: str
    password: str

class Show_user(BaseModel):
    id: int
    name: str
    email: str
    class Config():
        orm_mode = True