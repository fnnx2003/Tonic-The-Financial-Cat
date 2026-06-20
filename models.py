from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()
class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(225), nullable=False)
    initial_balance = Column(Float, default=0.0)
    transactions = relationship("Transactions", back_populates="user", cascade="all, delete-orphan")
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
class Transactions(base):
    __tablename__ = "Transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(10), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(String(225))
    date = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="transactions")
    def __repr__(self):
        return f"<Transactions(types='self.type', amount='self.amount', category='self.category')>"
def init_db(db_url="sqlite:///tonic_finance.db"):
    engine = create_engine(db_url, echo=True)
    base.metadata.create_all(engine)

if __name__ == "__main__":
    print("מייצר את בסיס הנתונים של טוניק...")
    init_db()
    print("בסיס הנתונים נוצר בהצלחה!")