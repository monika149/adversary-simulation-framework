# add_task.py
from database import SessionLocal
import models

db = SessionLocal()

# Replace with the actual agent_id you got
agent_id = 1

new_task = models.Task(
    agent_id=agent_id,
    command="whoami",
    status="pending"
)

db.add(new_task)
db.commit()
print(f"Added task for agent {agent_id}")
