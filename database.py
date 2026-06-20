from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, engine
from models import User, Transactions, init_db
engine = create_engine("sqlite:///tonic_finance.db", echo=True)
sessionlocal = sessionmaker(bind=engine)
if __name__ == "__main__":
    username = input("Enter a username:\n")
    email = input("Enter your Email:\n")
    password = input("Enter a password:\n")
    initial_balance = float(input("Enter your starting balance:\n"))
def create_user(username, email, password, initial_balance):
    with sessionlocal() as session:
        with session.begin():
            new_user = User(username=username, email=email, password=password, initial_balance=initial_balance)
            session.add(new_user)
            session.commit()
db = scoped_session(sessionlocal)
def create_transtacion(type, amount, category, description, date):
    with sessionlocal() as session:
        with session.begin:
            new_transaction = Transactions(type=type, amount=amount, category=category, description=description, date=date)
            session.add(new_transaction)
            session.commit()
def result():
    with sessionlocal() as session:
        user_data = session.query(User).all()
        print(f"the {user_data} is")
create_user(username, email, password, initial_balance)
print(result())
