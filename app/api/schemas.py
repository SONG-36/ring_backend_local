from pydantic import BaseModel

class UserData(BaseModel):
    sleep_hours: int
    steps_walked: int