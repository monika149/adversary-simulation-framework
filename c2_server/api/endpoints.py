from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register_agent")
def register_agent(agent: schemas.AgentRegister, db: Session = Depends(get_db)):
    new_agent = models.Agent(
        hostname=agent.hostname,
        ip=agent.ip,
        os=agent.os,
        last_seen=datetime.now()
    )
    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)
    return {"agent_id": new_agent.id}

@router.post("/get_task")
def get_task(data: schemas.TaskFetch, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter_by(agent_id=data.agent_id, status="pending").first()
    if task:
        task.status = "assigned"
        db.commit()
        return {"task_id": task.id, "command": task.command}
    return {"task_id": None, "command": None}

@router.post("/submit_result")
def submit_result(data: schemas.TaskSubmit, db: Session = Depends(get_db)):
    result = models.Result(
        task_id=data.task_id,
        output=data.output
    )
    task = db.query(models.Task).filter_by(id=data.task_id).first()
    task.status = "completed"
    db.add(result)
    db.commit()
    return {"message": "Result submitted"}
