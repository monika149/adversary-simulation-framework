from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from c2_server.database import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String)
    ip = Column(String)
    os = Column(String)
    last_seen = Column(DateTime, default=func.now())

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    command = Column(Text)
    status = Column(String, default="pending")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    output = Column(Text)
    timestamp = Column(DateTime, default=func.now())

class Port(Base):
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agent.id'))
    port = Column(Integer)
    protocol = Column(String(10))
    service =Column(String(100))

    def __repr__(self):
        return f"<Port {self.port}/{self.protocol} - {self.service}>"
