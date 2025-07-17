# utils/init_db.py
from c2_server.database import Base, engine
import c2_server.models

Base.metadata.create_all(bind=engine)
print("[+] Tables created.")
