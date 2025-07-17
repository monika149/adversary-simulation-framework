from pydantic import BaseModel
from typing import Optional

class AgentRegister(BaseModel):
    hostname: str
    ip: str
    os: str

class TaskFetch(BaseModel):
    agent_id: int

class TaskSubmit(BaseModel):
    task_id: int
    output: str
