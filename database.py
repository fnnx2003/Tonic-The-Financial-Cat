from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, engine
from models import User, Transactions, init_db
create_engine("sqlite:///tonic_finance.db", echo=True)
sessionlocal = sessionmaker(bind=engine)
if __name__ == "__main__":
    username = input("Enter a username:\n")
    email = input("Enter your Email:\n")
    password = input("Enter a password:\n")
    initial_balance = float(input("Enter your starting balance:\n"))
def create_user(username, email, password, initial_balance):
    with sessionlocal() as session:
        with session.begin():
            new_user = User(username=username, email=email, password=password, initial_balance=initial_balance, nullable=False)
            session.add(new_user)
            session.commit()
db = scoped_session(sessionlocal)
def result():
    with sessionlocal() as session:
        users = session.query(User).all()
        for user in users:
            print(user)
print(result())
