from pydantic import BaseModel
class User(BaseModel):
   id: int
   nombre: str
   correo: str
  
   